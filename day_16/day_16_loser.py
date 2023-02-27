from datetime import datetime
from datetime import timedelta

now = datetime.now()
print("--------------listen to day 16, loser, ayreon--------------")
print(f"now is", now)

formatted_now = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted_now)

date_string = "27 january, 2023"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

time1 = timedelta(weeks = 8, days = 2, hours = 7)
time2 = timedelta(weeks = 52)
rest_time = time2 - time1
print(f"time till new year", rest_time)

"""you can use timedate, to show everything to do with time, for example how much time rests for an event, calculate ages and more