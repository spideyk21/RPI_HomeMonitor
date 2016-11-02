#!/usr/bin/env python3
#title           : rpi_homemonitor.py
#description     : Monitor Movement, Temperature, Power Status, and Operate Relay (future)
#author          : J.Pudlo (spideyk21)
#date            : 10/24/2016
#version         : 0.1
#
#usage           : add to crontab, i.e. @reboot /[location]/rpi_homemonitor.py
#
#python_version  : 3.0
#notes			 : uses gpiozero (https://gpiozero.readthedocs.org/)
#				 : requires curl (sudo apt-get install curl) for pushbullet
#				 : https://learnraspi.com/2016/04/12/get-notifications-raspberry-pi-pushbullet/
#				 : http://www.raspberrypi-spy.co.uk/2015/07/robotsentry-home-security-system-part-1/
#==============================================================================

from RPi import GPIO
from gpiozero import Button
from gpiozero import MotionSensor
from gpiozero import LED
import time
import os

led_pwr = LED(x)
led_active = LED(x)
pir = MotionSensor(18)
button_active = Button(x) #on/off slide switch
pushbullet = xxxxx #pushbullet token

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
#def motion():
#	pir.wait_for_motion()
#	led_active.on() #when motion turn LED on
#	print("Motion Detected!")
#	#pushbullet send notification
#	#option - take picture if camera connected
#	led_active.off() #turn LED off after notification is sent

#def temperature():
	
	
# -----------------------
# Main Script
# -----------------------

pwr_led.on() #turn on power led to notify program is running

while true:
	while button_active = true:
		pir.wait_for_motion()
		led_active.on() #when motion turn LED on
		print("Motion Detected!")
		#pushbullet send notification
		#option - take picture if camera connected
		led_active.off() #turn LED off after notification is sent
		sleep(60) #delay for 60 seconds
	