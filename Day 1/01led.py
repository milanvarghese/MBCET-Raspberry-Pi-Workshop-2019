import RPi.GPIO as led
led.setmode(led.BOARD)
import time

led_pin=3

led.setwarnings(False)
led.setup(led_pin,led.OUT)

while(1):
    led.output(led_pin,1)
   