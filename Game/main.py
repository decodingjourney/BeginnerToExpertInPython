from player import Player

from enemy import Enemy

anand = Player("Anand")

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

random_enemy = Enemy("Basic Enemy", 12, 1)
print(random_enemy)

random_enemy.take_damage(4)
print(random_enemy)

random_enemy.take_damage(4)
print(random_enemy)

random_enemy.take_damage(5)
print(random_enemy)