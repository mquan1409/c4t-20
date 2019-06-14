import calendar
y = int(input("year?"))
m = int(input("month?"))
print(calendar.monthrange(y,m)[1])

