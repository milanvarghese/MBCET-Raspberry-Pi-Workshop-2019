import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

led=[3,5,7]
pwm[]=[0,0,0]
for x in led:
    GPIO.setup(x,GPIO.OUT)
    pwm[x]=GPIO.PWM(x,100)

print("\nPress Ctl C to quit\n")

pwm.start(dc)
while True:
    dc=0
    for x in pwm:
        for dc in range(0,101,5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(.01)
            print(dc)
        for dc in range(95,0,-5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(.01)
        print(dc)