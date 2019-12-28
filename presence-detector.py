#coding=utf-8

import subprocess

from sense_hat import SenseHat

sense = SenseHat()

from time import sleep

from datetime import datetime

import logging

logging.basicConfig(filename='/home/pi/presence/presence-detector.log',level=logging.INFO,format='%(asctime)s - %(message)s')
logging.info('Starting presence detector')

#names  of device owners
names = ["Frank", "Andrew_phone"]

#MAC addresses of  devices 

macs= ["d4:28:d5:37:7e:a2","2c:0e:3d:92:79:ef"]



def arp_scan():
	try:
		time= datetime.now()
		output = subprocess.check_output("sudo arp-scan -l", shell=True)
        	for i in range (len(names)):
			result = names[i]
			if macs[i] in output:
				result= result+" is home"
			else:
				result=result+" is not home"
			print (time.strftime("%H:%M:%S"), result)
			sense.show_message(result) 
	except Exception as e:
		logging.error(e)

arp_scan()
sleep(30) #moved the sleep to avoid the function running twice at startup

while  True:
	arp_scan()
