from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        print(self.herd.dinosaurs_list[0].name,
              self.fleet.robots_list[2].weapon.attack_power)
        pass

    def display_welcome(self):  # print welcome to Robots VS Dinosaurs
        pass

    def battle(self):
        pass

    def dino_turn(self, dinosaur):  # will be computer generated responses
        pass

    def robo_turn(self, robot):  # print input, list options
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):  # print congrats you are the winner!
        pass
