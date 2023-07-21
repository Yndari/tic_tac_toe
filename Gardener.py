class Tomatoe:
    states = ['Отсутствует', 'Цветение', 'Зеленый', 'Красный']
    idx = 0
    def __init__(self):
        self.state = self.states[self.idx]


    def grow(self):
        if self.idx < 3:
            self.idx += 1

    def is_ripe(self):
        return True if self.state.idx == 3 else False

    def show_info(self):
        print('State: ', self.state)


class Bush:
    def __init__(self, n):
        self.n = n
        self.tomatoes = [Tomatoe()for i in range(n)]

    def grow_all(self):
        for tomatoe in self.tomatoes:
            Tomatoe.grow()

    def ripe_all(self):
        return all([t.is_ripe() for t in self.Tomatoe])

    def show_info(self):
        print('Кол-во помидоров: ', self.n)

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self.plant = plant

    def work(self,):
        self.plant.grow_all()

    def gather_crop(self):
        if self.plant.ripe_all():
            self.plant.tomatoes = []
            print('Урожай собран')

       def knowledge_base(self):
        print('Рекомендации к работе в саду: ')
        print('1.Поливайте растения вовремя')
        print('1.Поливайте растения вовремя')

bush = Bush(4)



