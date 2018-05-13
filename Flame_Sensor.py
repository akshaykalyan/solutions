import RPi.GPIO as GPIO
import time
import os
"""A flame detector is a sensor designed to detect and respond to the presence of a flame or fire. Responses to a detected flame depend on the installation,
but can include sounding an alarm, deactivating a fuel line (such as a propane or a natural gas line), and activating a fire suppression system. When used in applications such as industrial furnaces, their role is to provide confirmation that the furnace is properly lit; in these cases they take no direct action beyond notifying the operator or control system.
A flame detector can often respond faster and more accurately than a smoke or heat detector due to the mechanisms it uses to detect the flame."""
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.IN)#######Digital input 
GPIO.setup(38,GPIO.OUT)######Buzzer
GPIO.setup(36,GPIO.OUT)######Green LED
GPIO.setup(33,GPIO.OUT)######Red Light
ch_flag=True
try:
    while True:
        if GPIO.input(40)==0:
            GPIO.output(38, False)
            if ch_flag==True:
                os.system('clear')
                print("By Akshay Kalyan")
                print("Normal")
                GPIO.output(33,True)
                GPIO.output(36,False)
                ch_flag=False
        if GPIO.input(40)==1:
            GPIO.output(38, True)
            if ch_flag==False:
                os.system('clear')
                print("By Akshay Kalyan")
                print("Fire Detected!!")
                GPIO.output(36,True)
                GPIO.output(33,False)
                ch_flag=True
except(KeyboardInterrupt):
    GPIO.cleanup()
