import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)

TRIG = 16 
ECHO = 18
#GPIO.setup(40,GPIO.OUT)
try:
    while(True):
        #print "Distance Measurement In Progress"
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG, False)
        #print "Waiting For Sensor To Settle"
        time.sleep(.2)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        #distance = round(distance, 2)
        os.system('clear')
        print("Demostration of Ultrasonic Sensor HC-sr04")
        print("By Akshay and Abhinav")
        print "Distance:",distance,"cm"
        if distance >70:
            GPIO.output(40,True)
        else:
            GPIO.output(40,False)
        if distance >50:
            GPIO.output(38,True)
        else:
            GPIO.output(38,False)
        if distance >40:
            GPIO.output(3,True)
        else:
            GPIO.output(3,False)
        if distance >30:
            GPIO.output(36,True)
        else:
            GPIO.output(36,False)
        if distance >20:
            GPIO.output(35,True)
        else:
            GPIO.output(35,False)
        if distance >10:
            GPIO.output(33,True)
        else:
            GPIO.output(33,False)
        time.sleep(.5)
except(KeyboardInterrupt):
    print("cleaning up..")
    GPIO.cleanup()
    time.sleep(2)
    os.system('clear')
