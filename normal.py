class Person:

    def __init__(self, name, health, damage, armor, is_alive, cooldown):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.is_alive = is_alive
        self.cooldown = cooldown

    def attack(self, enemy):
        enemy.health = enemy.health - (self.damage - enemy.armor)
        self.cooldown -= 1
        print(f"{self.name} атакует {enemy.name} на {self.damage - enemy.armor} урона!")
        print(f"{enemy.name} осталось {enemy.health} здоровья")

    def heal(self):
        self.cooldown += 5
        self.health += 10

    def battle(self, enemy):
        print(f"{self} vs {enemy}")
        while self.is_alive or enemy.is_alive:
            self.attack(enemy)
            if enemy.health <= 0:
                enemy.is_alive = False
            if self.cooldown == 0:
                self.heal()
            if not enemy.is_alive:
                break
            enemy.attack(self)
            if self.health <= 0:
                self.is_alive = False
            if enemy.cooldown == 0:
                enemy.heal()
                if not self.is_alive:
                    break
        if self.is_alive:
            print("Победа!")
        else:
            print("Поражение!")


class Player(Person):
    def __init__(self, health, damage, armor):
        super().__init__()
        self.name = "Игрок"
        self.health = health
        self.damage = damage
        self.armor = armor
        self.is_alive = True
        self.cooldown = 0


class Enemy(Person):
    def __init__(self, health, damage, armor):
        super().__init__()
        self.name = "Враг"
        self.health = health
        self.damage = damage
        self.armor = armor
        self.is_alive = True
        self.cooldown = 0


hero = Player(100, 15, 9)
devil = Enemy(80, 10, 5)
hero.battle(devil)
