#!/bin/bash
cd /home/ec2-user/app
pkill -f app.py || true
nohup python3 app.py > app.log 2>&1 &
