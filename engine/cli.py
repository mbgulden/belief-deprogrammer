"""
Belief Deprogrammer CLI + API

Usage:
  # Generate from chart JSON
  python3 cli.py generate --chart chart.json --tier comprehensive
  
  # Generate short version
  python3 cli.py generate --chart chart.json --tier short
  
  # Generate directly from birth data (calls HD engine)
  python3 cli.py generate-from-birth --name "Michael" --year 1989 --month 12 --day 10 \\
      --hour 17 --minute 7 --lat 34.2694 --lon -118.7815 --timezone America/Los_Angeles
"""

import sys
import json
import argparse
from pathlib import Path

# Add engine to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from engine.generator import WorkbookGenerator


def generate_from_chart(chart_path: str, tier: str = "comprehensive", output: str = None):
    """Generate workbook from a chart JSON file."""
    with open(chart_path) as f:
        chart = json.load(f)

    gen = WorkbookGenerator(chart)
    gen.generate(tier=tier)
    markdown = gen.format_markdown(tier=tier)

    if output:
        with open(output, 'w') as f:
            f.write(markdown)
        print(f"Workbook written to {output}")
    else:
        print(markdown)

    return markdown


def generate_from_birth(name: str, year: int, month: int, day: int,
                        hour: float, minute: int, lat: float, lon: float,
                        timezone: str, tier: str = "comprehensive", output: str = None):
    """Generate workbook directly from birth data by calling the HD engine."""
    import requests

    # Call HD engine
    resp = requests.post('http://localhost:8000/v1/natal/noauth', json={
        "name": name,
        "year": year,
        "month": month,
        "day": day,
        "hour": int(hour),
        "minute": int(minute),
        "latitude": lat,
        "longitude": lon,
        "timezone": timezone,
    }, timeout=30)

    if resp.status_code != 200:
        print(f"HD Engine error: {resp.status_code} {resp.text[:200]}")
        sys.exit(1)

    chart = resp.json()
    gen = WorkbookGenerator(chart)
    gen.generate(tier=tier)
    markdown = gen.format_markdown(tier=tier)

    if output:
        with open(output, 'w') as f:
            f.write(markdown)
        print(f"Workbook written to {output}")
    else:
        print(markdown)

    return markdown


def main():
    parser = argparse.ArgumentParser(description="Belief Deprogrammer")
    sub = parser.add_subparsers(dest="command")

    gen = sub.add_parser("generate", help="Generate from chart JSON")
    gen.add_argument("--chart", required=True)
    gen.add_argument("--tier", default="comprehensive", choices=["short", "comprehensive"])
    gen.add_argument("--output", default=None)

    birth = sub.add_parser("generate-from-birth", help="Generate from birth data")
    birth.add_argument("--name", required=True)
    birth.add_argument("--year", type=int, required=True)
    birth.add_argument("--month", type=int, required=True)
    birth.add_argument("--day", type=int, required=True)
    birth.add_argument("--hour", type=float, required=True)
    birth.add_argument("--minute", type=int, default=0)
    birth.add_argument("--lat", type=float, required=True)
    birth.add_argument("--lon", type=float, required=True)
    birth.add_argument("--timezone", required=True)
    birth.add_argument("--tier", default="comprehensive", choices=["short", "comprehensive"])
    birth.add_argument("--output", default=None)

    args = parser.parse_args()

    if args.command == "generate":
        generate_from_chart(args.chart, args.tier, args.output)
    elif args.command == "generate-from-birth":
        generate_from_birth(
            args.name, args.year, args.month, args.day,
            args.hour, args.minute, args.lat, args.lon, args.timezone,
            args.tier, args.output
        )
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
