class Car:

    def __init__(self, color = None, type = None, year = None):
        self.color = color
        self.type = type
        self.year = year

    def run(self):
        print('Автомобиль заведен')

    def off(self):
        print('Автомобиль заглушен')

    def assign_year(self):
        if self.year:
            print(f'{self.year}')

    def assign_type(self):
        if self.type:
            print(f'{self.type}')

    def assign_color(self):
        if self.color:
            print(f'{self.color}')

machine = Car('green', 'bmw', '2022')

machine.run()
machine.off()

machine.assign_year()
machine.assign_type()
machine.assign_color()