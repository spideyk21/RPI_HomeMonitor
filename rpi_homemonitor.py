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
#				 : requires Adafruit Python DHT Library (https://github.com/adafruit/Adafruit_Python_DHT.git)
#				 : https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/software-install-updated
#				 : https://learnraspi.com/2016/04/12/get-notifications-raspberry-pi-pushbullet/
#				 : http://www.raspberrypi-spy.co.uk/2015/07/robotsentry-home-security-system-part-1/
#				 : http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
#==============================================================================

from RPi import GPIO
from gpiozero import Button
from gpiozero import MotionSensor
from gpiozero import LED
import time
import os
import Adafruit_DHT

#led_pwr = LED(x)
#led_active = LED(x)
pir = MotionSensor(18)
#button_active = Button(x) #on/off slide switch

dht_sensor = Adafruit_DHT.DHT11 #Sensor Type
dht_pin = 23 #GPIO number for Sensor

#pushbullet = xxxxx #pushbullet token

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
		
#gpio_header_rev = GPIO.RPI_INFO['P1_Revision']

#if gpio_header_rev == 1 or gpio_header_rev == 2:
#	switch_pin = 7
#elif switch_pin = 21

#button = Button(switch_pin) #set gpio number based on board rev.

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

#turn on power led to notify program is running
#pwr_led.on()

#grab sensor reading
# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')


while True:
#	while button_active = true:
		pir.wait_for_motion()
		#led_active.on() #when motion turn LED on
		print("Motion Detected!")
		#pushbullet send notification
		#option - take picture if camera connected
		#led_active.off() #turn LED off after notification is sent
		time.sleep(5) #delay in seconds
	
