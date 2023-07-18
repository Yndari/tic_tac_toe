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


# Jim_Kerry = Giraffe()

class Grass():
    def __init__(self, value =0):
        self.value = value

# name= Grass(90)
# print(Jim_Kerry.eat(name))
# print (Jim_Kerry.eat(name))
# print(Jim_Kerry.hunger)

class Knight:
    def __init__(self, sword=False):
        self.sword = sword
        self.hp = 100
        self.damage = self.set_damage()


    def set_damage(self):
        if self.sword:
            self.damage = 20
        else:
            self.damage = 5
        return self.damage

class BossKninght(Knight):
    def __init__(self, sword=False, super_damage=0):
        super().__init__(sword)
        self.super_damage = super_damage


player = Knight(True)
boss = BossKninght(True, super_damage=15)
# print(player.damage)
# print(boss.damage)1

while player.hp > 0 and boss.hp > 0:
    action = input("Если готовы, нажмите 1 ")
    if action == '1':
        print("Бьет рыцарь!")
        boss.hp -= player.damage
        print(f'Жизни Босса: {boss.hp}')
        print("Босс!")
        player.hp -= boss.damage + boss.super_damage
        print(f'Жизни рыцаря: {player.hp}')


if player.hp > 0:
    print('Рыцарь победил!')
else:
    print('Босс победил')




