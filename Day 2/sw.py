import RPi.GPIO as sw
sw.setmode(sw.BOARD)
import time
sw.setwarnings(False)

sw_pin=5
led_pin=7
sw.setup(sw_pin,sw.IN,pull_up_down=sw.PUD_UP)

sw.setup(led_pin,sw.OUT)
sw.output(led_pin,0)

while(1):
    x=sw.input(sw_pin)
    if x==0:
        while(1):
           sw.output(led_pin,1)
           time.sleep(.05)
           sw.output(led_pin,0)
           time.sleep(.05)
           x=sw.input(sw_pin)
           if x==1:
               break;
    else:
        sw.output(led_pin,0)