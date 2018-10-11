from datetime import date, timedelta, datetime

today = date.today()
print(today)
print(type(today))
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())

d2 = date(day=31, month=12, year=2017)
print(d2)
print(type(d2))

oneweekdelta = timedelta(weeks=1)
oneweekhencedate = today + oneweekdelta

print(oneweekhencedate)
print(type(oneweekhencedate))

taskcompletetion = (2, 3)
twoweekdelta = timedelta(weeks=taskcompletetion[0], days=taskcompletetion[1])

twoweekdate = today + twoweekdelta

print(twoweekdate)
print(type(twoweekdate))

now = datetime.now()
print(now)
print(type(now))

nowtime = datetime.time(now)
print(nowtime)
print(type(nowtime))

print(nowtime.hour)
print(nowtime.minute)

print(today)
print(today.strftime('%m/%d/%Y'))
