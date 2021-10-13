from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        pass

    def display_welcome(self):  # print welcome to Robots VS Dinosaurs
        pass

    def battle(self):
        self.fleet.robots_list[0].attack(self.herd.dinosaurs_list[1])
        self.herd.dinosaurs_list[1].attack(self.fleet.robots_list[0])
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
