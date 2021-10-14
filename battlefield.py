from fleet import Fleet
from herd import Herd

game_over = False


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        pass

    def display_welcome(self):
        print("Welcome to ROBOTS VS DINOSAURS!!!!")
        pass

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        self.herd.dinosaurs_list[0].attack(self.fleet.robots_list[0])
        if self.fleet.robots_list[0].health <= 0:
            self.fleet.robots_list.pop(0)
        pass

    def robo_turn(self, robot):
        self.fleet.robots_list[0].attack(self.herd.dinosaurs_list[0])
        if self.herd.dinosaurs_list[0].health <= 0:
            self.herd.dinosaurs_list.pop(0)
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):  # print congrats you are the winner!
        pass
