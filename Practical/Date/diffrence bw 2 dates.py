from datetime import datetime

start_date = datetime(2024, 11, 15)
end_date = datetime(2024, 12, 15)


difference = (end_date - start_date).days

print("Number of days between November 15 and December 15:", difference)
