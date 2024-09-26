

import datetime 

today=datetime.date.today()
prev_date=today-datetime.timedelta(days=45)
print(prev_date)