# cities = ["Bangalore", "Delhi", "Chennai", "Mumbai", "Patna", "Hydrabad", "You are such a basturd"]
#
# with open("cities.txt", 'w') as city_name:
#     for city in cities:
#         print(city, file=city_name)
#
# cities = []
#
# with open("cities.txt",'r') as city_name:
#     for city in city_name:
#         cities.append(city.strip('\n'))
#
# print(cities)
#
# for city in cities:
#     print(city)

imelda = "more imelda", "May", "2011", (
    (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish town waltz")
)

with open("imelda.txt", 'w') as imelda_file:
    print(imelda, file=imelda_file)