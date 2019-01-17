# t = "a", "b", "c"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))


# metallica = "Riding the Lightning", "Metallica", "1984"
#
# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
#
# # metallica[0] = "Master of music"
# metallica = metallica[0], "Mettalic", metallica[2]
# print(metallica)
#
# metallica2 = ["Riding the Lightning", "Metallica", "1984"]
# print(metallica2)
# metallica2[0] = "Master of puppets"
# print(metallica2)


# a = b = c = d = 12
# print(c)
#
# a, b = 12,23
# print(a,b)
# metallica2.append("Rock")
# title,artist,year = metallica2
# print(title)
# print(artist)
# print(year)

bollywood = "movie", "dialogue", "lyrics", "song",(
    (1, "Sonu Nigam"), (2, "Arijit"), (3,"Udit Narayan"), (4, "Jubin Nautiyal")
)

print(bollywood)

# name,dia,lyr,son,singer1,singer2, singer3, singer4 = bollywood
# print(name)
# print(dia)
# print(lyr)
# print(son)
# print(singer1)
# print(singer2)
# print(singer3)
# print(singer4)

name,dia,lyr,son,singer = bollywood
print(name)
print(dia)
print(lyr)
print(son)
for song in singer:
    number,singername = song
    print("\tSingerNumer {}, SingerName {} ".format(number,singername))

