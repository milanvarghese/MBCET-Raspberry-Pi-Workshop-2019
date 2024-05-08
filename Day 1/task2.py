import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import time

GPIO.setup(5,GPIO.OUT)
pwm=GPIO.PWM(5,100)
GPIO.setwarnings(False)

dc=0
pwm.start(dc)
while True:
    for dc in range(0,101,5):
        pwm.ChangeDutyCycle(dc)
        time.sleep(.5)
        print(dc)
    for dc in range(95,0,-5):
        pwm.ChangeDutyCycle(dc)
        time.sleep(.5)
        print(dc)