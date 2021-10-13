from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        dino_1 = Dinosaur("T-Rex", 4)
        dino_2 = Dinosaur("Velociraptor", 6)
        dino_3 = Dinosaur("Triceritops", 5)
        self.dinosaurs.extend([dino_1, dino_2, dino_3])
