class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weeee, it's really fun flying")
        elif self.ratio == 1:
            print("It's hard, But i can definitely fly")
        else:
            print("I thing i am fine walking")

class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin!")


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
    # test_duck(donald)
    #
    # peng = Penguin()
    # test_duck(peng)
