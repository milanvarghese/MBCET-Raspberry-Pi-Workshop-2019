import RPi.GPIO as led
led.setmode(led.BOARD)
import time

led.setwarnings(False)

pin=[3,5,7,11,13,15,19,21]
num=[[5,7,11,13,15,19],[11,19],[7,11,3,13,15],[7,11,3,19,15],[5,3,11,19],[7,5,3,19,15],[7,5,3,13,15,19],[7,11,19],[3,5,7,11,13,15,19],[3,5,7,11,19]]


for x in pin:
    led.setup(x,led.OUT)

def off():
    for x in pin:
        led.output(x,0)
    
ind=0
while True:
    ind=int(input("Enter an number between 0-9: "))
    off()
    
    for y in range(len(num[ind])):
        led.output(num[ind][y],1)


