import RPi.GPIO as led
led.setmode(led.BOARD)
import time

led_pin1=[3,5,7,11]
led_pin2=[13,15,19,21]
led_pin2.reverse()

led.setwarnings(False)

for x in led_pin1:
    led.setup(x,led.OUT)
for x in led_pin2:
    led.setup(x,led.OUT)

while(1):
    for x in led_pin1:
        led.output(x,1)
        led.output((2*x)+1,1)
        time.sleep(0.1)
    for x in led_pin2:
        led.output(y,1)
        led.output((2*x)+1,0)
        time.sleep(.1)
    led_pin1.revese()
    led_pin2.reverse()