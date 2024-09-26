import datetime

current_date=datetime.datetime.now()
num_days=datetime.timedelta(days=45)
print('45 days before=',current_date-num_days)
