import duck

flock = duck.Flock()
donald = duck.Duck()
diasy = duck.Duck()
duck3 = duck.Duck()
duck4 = duck.Duck()
duck8 = duck.Mallard()
# duck8 = duck.Penguin()
duck5 = duck.Duck()
duck6 = duck.Duck()
duck7 = duck.Duck()

flock.add_duck(donald)
flock.add_duck(diasy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(duck8)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)


flock.migrate()