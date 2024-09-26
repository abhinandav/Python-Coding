import datetime

print(datetime.datetime.now())
print(datetime.datetime(2003,1,29))


# formating as string
print(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))

# diffrence
date1=datetime.datetime(2003,1,29)
date2=datetime.datetime.now()
print(date2-date1)


# add date
date2=datetime.datetime.now()
date1=datetime.timedelta(days=45)
# print(date1+date2)


# current date

print(datetime.date.today())
print(datetime.datetime.now().date())


import time

current_timestamp = int(time.time())
print("Current Unix timestamp:", current_timestamp)
