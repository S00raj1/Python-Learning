# # Importing date from datetime
#
# from datetime import date
#
# date_1 = date(1999,12,31)
# date_2 = date(year=2000,month=7, day= 9)
#
# print(date_1)
# print(date_2)
#
# # Importing time from Datetime
# from datetime import time
# time_1 = time(5,25,50)
# time_2 = time(hour = 11, minute= 45, second=50)
# time_2 = time(hour = 11, minute= 45, second=50, microsecond=109)
#
# print(time_1)
# print(time_2)
#
#
# # importing datetime from datetime
# from datetime import datetime
# datetime_1 = datetime(1999,12,24,4,55,12)
# datetime_2 = datetime(1998,12,24,5,12,45,200)
#
# print(datetime_1)
# print(datetime_2)

# importing timedelta from datetime
from datetime import timedelta

time_delta1 = timedelta(5,55,25,1000,25,4,3)
xyz = timedelta(2,1,100,10,10,24,5)
time_delta2 = timedelta(40)
print(time_delta1)
print(time_delta2)
print(xyz)

# importing timezoneinfo from datetime
from datetime import timezone

time_zone = timezone(offset=timedelta(hours=10,minutes=15))
time_zone1 = timezone(offset=timedelta(hours=23,minutes=40))

print(time_zone)
print(time_zone1)
from datetime import date

date_time1 = date(2023,5,28)
date_time2 = date_time1 - date(1997,5,13)
date_time2 = (date_time2/365)
print(date_time2)

from datetime import datetime
dayss = datetime.strptime('1999/7/9', '%Y/%m/%d')
print(dayss)


# from datetime import date, datetime
d1 = date(1999,7,9)

d2 = d1.strftime('%Y %m %d')
d3 = d1.strftime('%Y %d %a')
print(d2)
print(d3)
