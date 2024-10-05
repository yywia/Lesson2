class Car:
    def __init__(self, speed, color, name, is_police):
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
        super().__init__(0, "black", "Town Car", False)

class SportCar(Car):
    def __init__(self):
        super().__init__(0, "red", "Sport Car", False)

class WorkCar(Car):
    def __init__(self):
        super().__init__(0, "blue", "Work Car", False)

class PoliceCar(Car):
    def __init__(self):
        super().__init__(0, "white and blue", "Police Car", True)

