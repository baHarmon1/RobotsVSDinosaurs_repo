from robot import Robot


class Fleet:
    def __init__(self):
        self.robots_list = []
        self.create_fleet()

    def create_fleet(self):
        robot_1 = Robot("Rob")
        robot_2 = Robot("Bzzz")
        robot_3 = Robot("4-OH-4")
        self.robots_list.extend([robot_1, robot_2, robot_3])
