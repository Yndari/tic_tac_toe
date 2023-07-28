class Tomatoe:
    states = ['Отсутствует', 'Цветение', 'Зеленый', 'Красный']
    idx = 0
    def __init__(self):
        self.state = self.states[self.idx]


    def grow(self):
        if self.idx < 3:
            self.idx += 1

    def is_ripe(self):
        return True if self.idx == 3 else False

    def show_info(self):
        print('State: ', self.state)


class Bush:
    def __init__(self, n):
        self.n = n
        self.tomatoes = [Tomatoe()for i in range(n)]

    def grow_all(self):
        for tomatoe in self.tomatoes:
            tomatoe.grow()

    def ripe_all(self):
        return all([t.is_ripe() for t in self.tomatoes])

    def show_info(self):
        print('Кол-во помидоров: ', len(self.tomatoes))



class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self.plant = plant

    def work(self,):
        self.plant.grow_all()
        print('Работаем...')

    def gather_crop(self):
        if self.plant.ripe_all():
            self.plant.tomatoes = []
        print('Урожай собран')

    def knowledge_base(self):
        print('Рекомендации к работе в саду: ')
        print('1.Поливайте растения вовремя')

bush = Bush(4)
g = Gardener('Sadovnik', bush)
g.knowledge_base()
g.work()
g.gather_crop()
bush.show_info()

if 0 >= self.body[0].y > HEIGHT or 0 >= self.body[0].x > WIDTH:
    copy_body = self.body
    self.body = []
    c = 3
    for i in copy_body:
        if c < 0:
            self.body.append(math.Vector2(c, i.y))
            c += 1


            def movie(self):
                if self.new_block == True:
                    copy_body = self.body[:]
                    copy_body.insert(0, copy_body[0] + self.direction)
                    self.body = copy_body
                    self.new_block = False
                else:
                    copy_body = self.body[:-1]
                    copy_body.insert(0, copy_body[0] + self.direction)
                    self.body = copy_body