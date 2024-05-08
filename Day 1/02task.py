import RPi.GPIO as led
led.setmode(led.BOARD)
import time

led_pin=[3,5,7,11,13,15,19,21]

led.setwarnings(False)

for x in led_pin:
    led.setup(x,led.OUT)

while(1):
    for x in led_pin:
        led.output(x,1)
        led_pin.reverse()
        led.output(x,1)
        time.sleep(0.1)
    for x in led_pin:
        led.output(x,0)
        led_pin.reverse()
        led.output(x,0)
        time.sleep(0.1)