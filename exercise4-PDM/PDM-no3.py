import calendar


def drawcalendar(month1, year1):
    return calendar.month(year1, month1, 0, 1)

if __name__ == '__main__':
    month2 = int(input("input month: "))
    year2 = int(input("input year: "))
    print("----------------------")
    print(drawcalendar(month2, year2))
