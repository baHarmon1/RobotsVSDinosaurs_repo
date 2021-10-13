from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from robot import Robot


robot_1 = Robot("Rob")
robot_2 = Robot("Bzzz")
robot_3 = Robot("4-OH-4")
fleet_1 = Fleet()
fleet_1.robots.extend([robot_1, robot_2, robot_3])

dino_1 = Dinosaur("T-Rex", 4)
dino_2 = Dinosaur("Velociraptor", 6)
dino_3 = Dinosaur("Triceritops", 5)
herd_1 = Herd()
herd_1.dinosaurs.extend([dino_1, dino_2, dino_3])
