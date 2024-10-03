class Toy:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
        self.purchase_materials()
        self.sewing()
        self.coloring()

    def purchase_materials(self):
        print(f"Закупка сырья для {self.name}")

    def sewing(self):
        print(f"Шьем {self.name}")

    def coloring(self):
        print(f"Окрашиваем {self.name} в {self.color}")

class PlushToys:
    def result(self):
        print(f"Создана плюшевая игрушка")

class CarToys:
    def result(self):
        print(f"Создана игрушечная машинка")

class ToyFactory(Toy):
    def __init__(self, name, model, color):
        super().__init__(name, model, color)
        if self.model == "plush_toy":
            PlushToys().result()
        elif self.model == "car_toy":
            CarToys().result()

test1 = ToyFactory("Медвежонок", "plush_toy", "коричневый")
test2 = ToyFactory("Спорт-кар", "car_toy", "красный")