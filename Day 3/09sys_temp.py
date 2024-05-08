import time
while (1):
    temp=int(open("/sys/class/thermal/thermal_zone0/temp").read())/(1e3)
    print(temp)
    time.sleep(.1)