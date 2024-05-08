import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

led1=[3,5,7,11,13,15,19,21]
GPIO.setwarnings(False)

for x in led1:
    GPIO.setup(x,GPIO.OUT)

print("\nPress Ctl C to quit\n")
dc=0
pwm.start(dc)
while True:
    for x in led1:
        pwm=GPIO.PWM(x,100)
        dc=0
        pwm.start(dc)
        
    for dc in range(0,101,5):
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.05)
        print(dc)
    for sc in range(95,0,-5):
        pwm.ChangeDutyCycle(dc)
        time.sleep(.05)
        print(dc)