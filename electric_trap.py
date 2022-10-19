import pico2d


class ElectronicTrap:
    def __init__(self):
        self.image = pico2d.load_image('resource/Electronic_Trap.png')
        self.x, self.y = 0, 0
        self.x1, self.y1 = 0, 0
        self.x2, self.y2 = 0, 0

    def set_location(self, x, y):
        self.x, self.y = x, y
        self.x1, self.y1 = x - 25, y - 25
        self.x2, self.y2 = x + 25, y + 25

    def draw(self, x, y):
        self.x, self.y = x, y
        self.image.draw(self.x, self.y)
