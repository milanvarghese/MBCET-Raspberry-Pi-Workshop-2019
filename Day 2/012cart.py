import RPi.GPIO as GPIO
import time

#Board Configuration
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

#Enabling RPi PINS
pins=[3,5,7,11,13]
for x in pins:
    GPIO.setup(x,GPIO.OUT)


m1a=7
m1b=11
m2a=5
m2b=3
en=13

GPIO.output(en,1)

while (1):
    time.sleep(2)
    GPIO.output(m1a,0)
    GPIO.output(m1b,1)
    GPIO.output(m2a,0)
    GPIO.output(m2b,1)
    time.sleep(2)
    GPIO.output(m1a,1)
    GPIO.output(m1b,0)
    GPIO.output(m2a,1)
    GPIO.output(m2b,0)
    time.sleep(2)
    
    