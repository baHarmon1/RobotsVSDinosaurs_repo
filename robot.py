from weapon import Weapon
from dinosaur import Dinosaur


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Sword", 5)

    def attack(self, dinosaur):
        self.enemy = dinosaur
        self.herd.dinosaurs_list[0].health = self.fleet.robots_list[0].weapon.attack_power - \
            self.herd.dinosaurs_list[0].health
        print(
            f"You attacked for {self.weapon.attack_power} damage, leaving the dinos health at {self.dinosaur.health}")
