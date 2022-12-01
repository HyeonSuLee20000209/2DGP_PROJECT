import pico2d

size = 25

class Ground:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.exist = True

        if Ground.image is None:
            Ground.image = pico2d.load_image('resource/Ground.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def get_bb(self):
        return self.x - size, self.y - size, self.x + size, self.y + size

    def handle_collision(self, other, group):
        pass

    def handle_collision_dir(self, other, group, dir):
        pass
