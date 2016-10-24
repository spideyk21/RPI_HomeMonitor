#!/usr/bin/env python3
#title           : rpi_homemonitor.py
#description     : Monitor Movement, Temperature, Power Status, and Operate Relay
#author          : J.Pudlo (spideyk21)
#date            : 10/24/2016
#version         : 0.1
#
#usage           : add to crontab, i.e. @reboot /[location]/rpi_shutdown.py
#
#python_version  : 3.0
#notes			 : uses gpiozero (https://gpiozero.readthedocs.org/)
#				 : requires curl (sudo apt-get install curl)
#				 : https://learnraspi.com/2016/04/12/get-notifications-raspberry-pi-pushbullet/
#				 : http://www.raspberrypi-spy.co.uk/2015/07/robotsentry-home-security-system-part-1/
#==============================================================================

from gpiozero import Button
from gpiozero import MotionSensor
from gpiozero import LED
from gpiozero import Relay
import time import sleep
import os

pwr_led = LED(x)
active_led = LED(x)
pir - MotionSensor(x)
button_active = Button(x)

# Check Board Revision
	#http://elinux.org/RPi_HardwareHistory
	# 0 = Compute Module
	# 1 = Rev 1
	# 2 = Rev 2
	# 3 = Model B+/A+
	# 4-9 & d-f = Model B2
	# 4-9 & d-f = Pi2 Model B
	# ? = Pi Zero
	# ? = Pi3
		
gpio_header_rev = GPIO.RPI_INFO['P1_Revision']

if gpio_header_rev == 1 or gpio_header_rev == 2:
	switch_pin = 7
elif switch_pin = 21

button = Button(switch_pin) #set gpio number based on board rev.

# -----------------------
# Functions
# -----------------------
def motion():
	pir.wait_for_motion()
	print("Motion Detected!")
	#pushbullet send notification

def temperature():
	
	
# -----------------------
# Main Script
# -----------------------
while true:
	
	
