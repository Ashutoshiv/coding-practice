import datetime

date = datetime.date(2025, 7, 13)
today = datetime.date.today()

time = datetime.time(22, 39, 0)

now = datetime.datetime.now()

now = now.strftime("%H:%M:%S \n%d-%m-%Y")

target_datetime = datetime.datetime(2030, 1, 2, 12, 29, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")

# print(date)
# print(today)
# print(time)
# print(now)