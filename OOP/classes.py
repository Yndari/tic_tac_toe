class Auto:
    def __init__(self, model, color, year): # инициализация
        self.model = model  # атрибут класса
        self.color = color # атрибут класса
        self.year = year # атрибут класса

    def display_info(self):
        '''Методы для вывода данных'''
        print(f'Model: {self.model}\nYear: {self.year}\nColor: {self.color}')


auto1 = Auto('Lexus', 'black', 2004)
auto2 = Auto('Toyota', 'black', 2015)
auto1.display_info()
auto2.display_info()
print(auto1.model)


print(auto1.color)

