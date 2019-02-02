class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

kelton = Kettle("Kelton", 8.99)
print(kelton.make)
print(kelton.price)

kelton.price = 12.99
print(kelton.price)

hamilton = Kettle("Hemilton", 209.99)
print(hamilton.make)
print(hamilton.price)

print("Models: {} = {}, {} = {}".format(kelton.make,kelton.price,hamilton.make,hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kelton, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kelton)
print(kelton.on)

kelton.power = 1.5
print(kelton.power)
# print(hamilton.power)

print(Kettle.power_source)
kelton.power_source = "gas"
print(kelton.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kelton.__dict__)
print(hamilton.__dict__)
