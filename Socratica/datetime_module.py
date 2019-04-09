import datetime

gvr = datetime.date(1956, 1, 31)
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)

mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)
print(mill + dt)

# Day-name, Month-name Day-#, Year
print(gvr.strftime("%A, %B %d, %Y"))

message = "Guido van Rossum was born on {:%A, %B %d, %Y}."
print(message.format(gvr))

launch_date = datetime.date(2017, 3, 30)
print(launch_date)
launch_time = datetime.time(22, 27, 0)
print(launch_time)
print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print(launch_datetime)
print(launch_datetime.year)
print(launch_datetime.month)
print(launch_datetime.day)
print(launch_datetime.hour)
print(launch_datetime.minute)
print(launch_datetime.second)

now = datetime.datetime.today()
print(now)
print(now.microsecond)

moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
print(type(moon_landing_datetime))
