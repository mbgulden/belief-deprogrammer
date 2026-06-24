#!/bin/bash
cd /home/ubuntu/work/belief-deprogrammer/engine
pkill -f "python.*server.py" || true
set -a
source .env
set +a
if python3 -c "import uvicorn" 2>/dev/null && grep -q "app = " server.py; then
    nohup python3 -m uvicorn server:app --host 0.0.0.0 --port 8092 >> server.log 2>&1 &
else
    nohup python3 server.py --port 8092 >> server.log 2>&1 &
fi
echo "Belief server restarted on port 8092"
