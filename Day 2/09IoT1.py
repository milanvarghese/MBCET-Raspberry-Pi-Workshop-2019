import datetime
import time

i=datetime.datetime.now()

print("current year: %s" %i.year)
time.sleep(.5)

print("current month: %s" %i.month)
time.sleep(.5)

print("current Day: %s" %i.day)
time.sleep(.5)

print("(dd/mm/yyyy): %s/%s/%s " %(i.day,i.month,i.year))
time.sleep(.5)

print("current hour= %s" %i.hour)
time.sleep(.5)

print("current minute= %s" %i.minute)
time.sleep(.5)

print("current second= %s" %i.second)
time.sleep(.5)

print("(hh:mm:s): %s:%s:%s " %(i.hour,i.minute,i.second))
time.sleep(.5)

while(1):
    i=datetime.datetime.now()
    print("(hh:mm:s): %s:%s:%s " %(i.hour,i.minute,i.second))
    time.sleep(.5)