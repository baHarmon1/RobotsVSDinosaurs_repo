class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack(self, robot):
        self.enemy = robot
        robot.health = (robot.health - self.attack_power)
        print(
            f"{robot.name} has been attacked by {self.name} for {self.attack_power} damage, leaving {robot.name}'s health at {robot.health}")
