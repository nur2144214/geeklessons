# OOP
# Class)

class Car:
    name = 'MERS'

    def __init__(self, model, year):
        self.model = model
        self.year = year

    def sayname(self):
        print(self.name)

    def __str__(self):
        return f'{self.model} {self.year}'

    def __len__(self):
        return len(self.model), len(self.year)
# обьект\экземпляр


mers = str(Car('bmw', 'i'))

print(len(mers))