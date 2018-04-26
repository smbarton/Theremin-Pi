#!/usr/bin/python3
# Filename: rangeFind.py

# sample script to read range values from Maxbotix ultrasonic rangefinder

from time import sleep
import maxSonarTTY

serialPort = "/dev/ttyAMA0"
maxRange = 5000  # change for 5m vs 10m sensor
sleepTime = 5
minMM = 9999
maxMM = 0

print("rangeFind.py...")

while True:
    print("Starting while loop...")
    mm = maxSonarTTY.measure(serialPort)
    if mm >= maxRange:
        print("Option 01...")
        print("no target")
        sleep(sleepTime)
        continue
    if mm < minMM:
        print("Option 02...")
        minMM = mm
    if mm > maxMM:
        print("Option 03...")
        maxMM = mm

    print("distance:", mm, "  min:", minMM, "max:", maxMM)
    sleep(sleepTime)
