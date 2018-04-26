#!/bin/sh
#startup_theremin.sh
xdotool key ctrl+c
sleep 1m
sleep 15s
cd /
cd home/pi/projects/theremin/startup
python3 rangeFind.py &
cat notePlayer.txt | sonic_pi
cd /
echo startup_theremin complete
