



def getdays(hrs,min,sec):
    hrsPrDay = 24
    minPrDay = 1440
    secPrDay = 86400

    Hdays = hrs/hrsPrDay
    Mdays = min/minPrDay
    Sdays = sec/secPrDay

    return Hdays + Mdays + Sdays

Hinput = int(input("input number of hours = "))
Minput = int(input("input number of minutes = "))
Sinput = int(input("input number of seconds = "))


print("total number of days = ", getdays(Hinput,Minput,Sinput))