from datetime import date
from datetime import time
from  datetime import datetime
from datetime import timedelta
def main():
    today = date.today()
    print("today's date is: ",today)
    print(today.day,today.month,today.year)
    print str(today.weekday())
    today1 = datetime.now()
    print(today1)
    t = datetime.time(datetime.now())
    print(t)
    wd=date.weekday(today)
    days= ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    print("Today is day number %d" % wd)
    print("which is a " + days[wd])
    print(today1.strftime("%a %d %b %y"))
    print(today1.strftime("%A %d %B %Y"))
    now= datetime.now() 
    print now.strftime("%c")
    print now.strftime("%x")
    print now.strftime("%X")
    print now.strftime("%I:%M:%S %p")
    print now.strftime("%H:%M") 
    print (timedelta(days=365, hours=8, minutes=15))
    print ("today is: " + str(datetime.now()))
    print ("one year from now it will be:" + str(datetime.now() + timedelta(days=365)))
    today = date.today() 
    nyd = date(today.year, 1, 1) 
    if nyd < today:
        print ("New Year day is already went by %d days ago" % ((today - nyd).days))
    
main()
