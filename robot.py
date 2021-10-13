from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Sword", 5)

    def attack(self, dinosaur):
        self.enemy = dinosaur
        dinosaur.health = (dinosaur.health - self.weapon.attack_power)
        print(
            f"{self.name} attacked {dinosaur.name} for {self.weapon.attack_power} damage, leaving {dinosaur.name}'s health at {dinosaur.health}")
