class Car:
    def __init__(self):
        self.speed = 0
        self.color = ""
        self.name = ""
        self.is_police = False

    def go(self):
        self.speed = 60
        print("Машина поехала")

    def stop(self):
        self.speed = 0
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула на {direction}")

class TownCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 0
        self.color = "black"
        self.name = "Town Car"
        self.is_police = False

class SportCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 0
        self.color = "red"
        self.name = "Sport Car"
        self.is_police = False

class WorkCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 0
        self.color = "blue"
        self.name = "Work Car"
        self.is_police = False

class PoliceCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 0
        self.color = "white and blue"
        self.name = "Police Car"
        self.is_police = True
