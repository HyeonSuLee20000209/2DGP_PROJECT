import pico2d


class ETrap:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y

        if ETrap.image is None:
            ETrap.image = pico2d.load_image('resource/ElectronicTrap.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 24, self.y - 24, self.x + 24, self.y + 24

    def handle_collision(self, other, group):
        pass
