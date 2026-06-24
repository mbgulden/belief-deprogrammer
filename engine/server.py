#!/usr/bin/env python3
"""Belief Deprogrammer — Web API Server

Exposes a single POST endpoint for generating personalized belief workbooks.
Calls the local HD Engine (localhost:8000) for chart computation, then runs
the belief generator.

Usage:
  python3 server.py --port 8090
"""

import sys
import json
import os
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

# Add engine to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from engine.generator import WorkbookGenerator
import requests

HD_ENGINE_URL = os.environ.get('HD_ENGINE_URL', 'http://localhost:8000')
TIER = 'comprehensive'
BELIEF_SERVER_SECRET = os.environ.get("BELIEF_SERVER_SECRET", "")


class BeliefAPI(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        origin = self.headers.get('Origin', '')
        if origin in ("https://humandesignengine.com", "https://www.humandesignengine.com"):
            self.send_header('Access-Control-Allow-Origin', origin)
            self.send_header('Access-Control-Allow-Credentials', 'true')

    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self._send_cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def _send_error(self, msg, status=400):
        self._send_json({"error": msg}, status)

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Belief-Secret')
        self.end_headers()

    def do_POST(self):
        if self.path != '/generate':
            self._send_error("Not found", 404)
            return

        content_type = self.headers.get('Content-Type', '')
        length = int(self.headers.get('Content-Length', 0))
        body_bytes = self.rfile.read(length) if length > 0 else b''

        body = {}
        if 'application/json' in content_type:
            try:
                body = json.loads(body_bytes)
            except json.JSONDecodeError:
                self._send_error("Invalid JSON")
                return
        else:
            try:
                body = json.loads(body_bytes)
            except json.JSONDecodeError:
                try:
                    from urllib.parse import parse_qs
                    parsed = parse_qs(body_bytes.decode('utf-8'))
                    body = {k: v[0] for k, v in parsed.items()}
                except Exception:
                    self._send_error("Invalid request body")
                    return

        # Authentication check
        secret = self.headers.get('X-Belief-Secret', '')
        tier_param = body.get('tier', 'free')

        if BELIEF_SERVER_SECRET and secret == BELIEF_SERVER_SECRET:
            tier = tier_param
        else:
            if tier_param in ('standard', 'comprehensive'):
                self._send_json({"error": "Unauthorized"}, 401)
                return
            tier = "free"

        # Validate required fields
        required = ['name', 'year', 'month', 'day', 'hour', 'minute',
                    'latitude', 'longitude', 'timezone']
        missing = [f for f in required if f not in body]
        if missing:
            self._send_error(f"Missing fields: {', '.join(missing)}")
            return

        # Call HD Engine for chart
        try:
            resp = requests.post(f'{HD_ENGINE_URL}/v1/natal/noauth', json={
                "name": body['name'],
                "year": body['year'],
                "month": body['month'],
                "day": body['day'],
                "hour": int(body['hour']),
                "minute": int(body['minute']),
                "latitude": body['latitude'],
                "longitude": body['longitude'],
                "timezone": body['timezone'],
            }, timeout=30)
        except requests.ConnectionError:
            self._send_error("HD Engine unreachable", 503)
            return

        if resp.status_code != 200:
            self._send_error(f"HD Engine error: {resp.status_code}", 502)
            return

        chart = resp.json().get('data', resp.json())

        # Generate workbook
        try:
            gen = WorkbookGenerator(chart)
            gen.generate(tier=tier)
            markdown = gen.format_markdown(tier=tier)
        except Exception as e:
            self._send_error(f"Generation error: {str(e)}", 500)
            return

        # Return results
        self._send_json({
            "name": body['name'],
            "type": chart.get('hd_type', 'Unknown'),
            "authority": chart.get('authority', 'Unknown'),
            "profile": chart.get('profile', 'Unknown'),
            "defined_centers": chart.get('defined_centers', []),
            "open_centers": chart.get('undefined_centers', []),
            "belief_pairs": len(gen.beliefs),
            "markdown": markdown,
        })

    def do_GET(self):
        if self.path == '/health':
            self._send_json({"status": "ok", "tier": TIER})
        else:
            self._send_error("Not found", 404)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8090)
    args = parser.parse_args()

    server = HTTPServer(('0.0.0.0', args.port), BeliefAPI)
    print(f"Belief Deprogrammer API on :{args.port}")
    print(f"HD Engine: {HD_ENGINE_URL}")
    server.serve_forever()
