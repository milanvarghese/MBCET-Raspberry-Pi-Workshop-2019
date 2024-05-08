import RPi.GPIO as led
led.setmode(led.BOARD)
import time

led_pin=[3,5,7]

led.setwarnings(False)

for x in led_pin:
    led.setup(x,led.OUT)

while(1):
    for x in led_pin:
        led.output(x,1)
        time.sleep(2)
    for x in led_pin:
        led.output(x,0)
        time.sleep(2)
    
