# import time
#
# print("The epoch on this system starts at "+time.strftime('%c', time.gmtime(0)))
#
# print("The current timezone is {0} with the offset of {1}".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("\t Daylight Time is in effect at this location")
#     print("\t Daylight time is :"+time.tzname[1])
#
# print("local time is "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# print("UTC time is "+time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))


import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())