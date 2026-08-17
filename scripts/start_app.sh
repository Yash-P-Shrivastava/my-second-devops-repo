#!/bin/bash
cd /home/ec2-user/app
pkill -f app.py || true
sudo nohup python3 app.py > /tmp/app.log 2>&1 &
