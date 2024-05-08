import RPi.GPIO as GPIO
import datetime
import time

#Setting up the boarg configuration
GPIO.setmode(GPIO.BOARD)

#setting up PIN
led_pin=7
GPIO.setup(led_pin,GPIO.OUT)

#Getting the current time
i=datetime.datetime.now()

#Getting the time
print("Enter Time: ")
RT_M=input("Enter Minute: ")
RT_S=input("Enter Second: ")

x=int(RT_S)
print (x)
GPIO.output(led_pin,0)

#Function
while(1):
    i=datetime.datetime.now()
    print("(hh:mm:s): %s:%s:%s " %(i.hour,i.minute,i.second))
    time.sleep(1)
    if i.second>=x:
        for i in range(5):
            GPIO.output(led_pin,1)
            time.sleep(.1)
            GPIO.output(led_pin,0)
            time.sleep(.1)
            