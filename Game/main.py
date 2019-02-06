from player import Player

from enemy import Enemy, Troll, Vampire, VampyreKing

# anand = Player("Anand")

# print(anand.name)
# print(anand.lives)
#
# anand.lives -= 1
# print(anand)
#
# anand.lives -= 1
# print(anand)
#
# anand.lives -= 1
# print(anand)
#
# anand.lives -= 1
# print(anand)
#
# anand.level = 2
# print(anand)
#
# anand.level += 5
# print(anand)
#
# anand.level = 3
# print(anand)

# random_enemy = Enemy("Basic Enemy", 12, 1)
# print(random_enemy)
#
# random_enemy.take_damage(4)
# print(random_enemy)
#
# random_enemy.take_damage(4)
# print(random_enemy)
#
# random_enemy.take_damage(5)
# print(random_enemy)

# troll = Troll("anand")
# print("Troll is {}".format(troll))
#
#
# another_troll = Troll("Ug")
# print("Another troll is {}".format(another_troll))
#
#
# brother = Troll("Brother")
# print("Brother is {}".format(brother))
#
# troll.grunt()
# another_troll.grunt()
# brother.grunt()
# brother.take_damage(10)
# print(brother)
#
#
# new_vampire = Vampire("Dangerous")
# print(new_vampire)
# new_vampire.take_damage(5)
# print(new_vampire)

print("_" * 40)

# while new_vampire.alive:
    # if not new_vampire.dodges():
    # new_vampire.take_damage(1)
    # print(new_vampire)

# new_vampire._lives = 0
# new_vampire._hit_points = 1
# print(new_vampire)


dracula = VampyreKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)

