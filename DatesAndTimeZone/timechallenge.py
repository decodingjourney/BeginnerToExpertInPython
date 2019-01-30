import datetime

import pytz

available_zones = {'1': "America/Atka",
                   '2': "America/Chicago",
                   '3': "Asia/Amman",
                   '4': "Africa/Tuniz",
                   '5': "Asia/Kolkata",
                   '6': "Australia/Adelaide",
                   '7': "Europe/London",
                   '8': "Japan",
                   '9': "US/Hawaii"}
print("Please choose the time zone (or 0 to Quit)")
for place in sorted(available_zones):
    print("\t\t{} . {}".format(place, available_zones[place]))


while True:
    choice = input()

    if choice == '0':
        break
    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(tz_to_display, world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print("The local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("The UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))