import datetime


class Mammals:
    def __init__(self, height, weight, year_of_birth):
        self.height = height
        self.weight = weight
        self.year_of_birth = year_of_birth
        self.age = self.set_age()


    def set_age(self):
        current_year = datetime.datetime.now().year
        self.age = current_year - self.year_of_birth
        return self.age



    def move(self):
        print("I'm moving")

    def make_noise(self):
        pass

    def eat(self):
        print("I'm eating")

class Giraffe():
    def __init__(self, hunger=100):
        self.hunger = hunger


    def make_noise(self):
        print('Hum')

    def eat(self, grass):
        if 20 < self.hunger <= 100:
            print("I'm hungry")
            self.hunger -= grass.value
        elif 10 <= self.hunger <= 20:
            print("I can eat")
            #self.hunger -= grass.value
        else:
            print("I'm full, thank you")
        return f'Hunger level: {self.hunger}'


 Jim_Kerry = Giraffe()

class Grass():
    def __init__(self, value =0):
        self.value = value

name= Grass(90)
print(Jim_Kerry.eat(name))
print (Jim_Kerry.eat(name))
print(Jim_Kerry.hunger)
#
# class Knight:
#     def __init__(self, sword=False):
#         self.sword = sword
#         self.hp = 100
#         self.damage = self.set_damage()
#
#
#     def set_damage(self):
#         if self.sword:
#             self.damage = 20
#         else:
#             self.damage = 5
#         return self.damage
#     def __add__(self, other):
#         return self.damage + other.damage
#
#
#
#
# class BossKninght(Knight):
#     def __init__(self, sword=False, super_damage=0):
#         super().__init__(sword)
#         self.super_damage = super_damage
#
# class MagicSword():
#     def __init__(self, damage, ready=True):
#         self.damage = damage
#         self.ready = ready
#     def __add__(self, other):
#         return self.damage + other.damage
#
#
#
#
#
#
#
# player = Knight(True)
# boss = BossKninght(True, super_damage=10)
# companion = MagicSword(60)
# print(player + companion)
# cooldawn = 0
#
#
# while player.hp > 0 and boss.hp > 0:
#
#     action = input("Если готовы, нажмите 1 ")
#     if action == '1':
#         cooldawn += 1
#         if cooldawn % 3 == 0:
#              print('Бьет рыцарь с магическим мечом!')
#              boss.hp -= player + companion
#         else:
#             print("Бьет рыцарь!")
#             boss.hp -= player.damage
#         print("Бьет Босс!")
#         player.hp -= boss.damage + boss.super_damage
#         if player.hp < 0:
#             player.hp = 0
#         elif boss.hp < 0:
#             boss.hp = 0
#         print(f'Жизни рыцаря:', player.hp, '\nЖизни Босса', boss.hp)
#
#
#     else:
#         break
#
#
#
#
# if player.hp == boss.hp:
#     print('Ничья')
# elif boss.hp > player.hp:
#     print(f'Побеждает Босс!')
# else:
#     print(f'Побеждает Рыцарь!')
#
#
# army = []
# for i in range(10):
#     army.append(Knight(True))

import math
math.pi

class Triangle():
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self, ):
        return round(self.a * self.h / 2, 3)



class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def perimetr(self):
        return (self.a + self.b) * 2

    def area (self):
        return self.a * self.b


class Circle:
    def __init__(self,r=0):
        self.r = r

    def area(self):
        return self.r**2 * math.pi

    def perimetr(self):
        return math.pi*2*self.r

# print(Rectangle(2, 4).area())
