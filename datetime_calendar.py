import datetime
from datetime import date,time,datetime
import calendar
import random
import time

#a = datetime.datetime.now()
b = calendar.month(2026,4)
c = calendar.calendar
d = datetime.now()
e = date.today()
#f = time(14,00,00)
print (d, "\n", b, "\n", e, "\n")
def getrandomdate(startdate,enddate):
    g = random.random()
    dateformat = "%d/%m/%Y"
    starttime = time.mktime(time.strptime(startdate, dateformat))

    endtime = time.mktime(time.strptime(enddate, dateformat))
    randomtime = starttime + g * (endtime - starttime)
    randomdate = time.strftime(dateformat, time.localtime(randomtime))
    return randomdate
print("random date =", getrandomdate("19/6/2009","30/6/2009"))