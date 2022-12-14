import pico2d


class ETrap:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.exist = True

        if ETrap.image is None:
            ETrap.image = pico2d.load_image('resource/ElectronicTrap.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 18, self.y - 18, self.x + 18, self.y + 18

    def handle_collision(self, other, group):
        pass

    def handle_collision_dir(self, other, group, dir):
        pass
