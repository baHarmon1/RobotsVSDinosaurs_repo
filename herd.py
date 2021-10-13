from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs_list = []
        self.create_herd()

    def create_herd(self):
        dino_1 = Dinosaur("T-Rex", 4)
        dino_2 = Dinosaur("Velociraptor", 6)
        dino_3 = Dinosaur("Triceritops", 5)
        self.dinosaurs_list.extend([dino_1, dino_2, dino_3])
