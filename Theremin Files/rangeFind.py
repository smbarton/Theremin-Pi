#!/usr/bin/python3
# Filename: rangeFind.py

#OSC message sender for SonicPi
from pythonosc import osc_message_builder
from pythonosc import udp_client

#for GPIO - Input from sensors
from gpiozero import DistanceSensor

#another way to play sounds with sonic pi
from psonic import*

from time import sleep

sensor_vol = DistanceSensor(echo=17, trigger=4) #right sensor = volume control
sensor_pitch = DistanceSensor(echo=19, trigger=6) #left sensor = pitch control

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559) #initialize osc sender

print("rangeFind.py...")
#uses psonic to play a note
#used here to confirm that the program has started properly
play(70)

while True:

    vol_raw = sensor_vol.distance
    pitch_raw = sensor_pitch.distance

    if vol_raw < 0.5 and pitch_raw < 0.5:
        pitch = round(pitch_raw * 100 + 40)
        volume = vol_raw * 2
        print("pitch : ", pitch, " | volume: " , volume)
        sender.send_message('/play_this', pitch)
        sender.send_message('/this_loud', volume)

        #use_synth(SAW)
        #play(pitch, amp=volume)
        
    sleep(0.1)

    ##For testing...
    #if vol_raw < 0.5:
    #    print("vol: ", round(sensor_vol.distance, 2))
    #if pitch_raw < 0.5:
    #    print("pitch: ", round(sensor_pitch.distance, 2))
    #print("vol: ", round(sensor_vol.distance, 2), "| pitch: ", round(sensor_pitch.distance, 2))
