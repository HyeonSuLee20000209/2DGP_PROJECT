import pico2d


class Spike:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y

        if Spike.image is None:
            Spike.image = pico2d.load_image('resource/Spike.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 22, self.y - 7, self.x + 20, self.y

    def handle_collision(self, other, group, dir):
        pass

    def handle_collision_dir(self, other, group, dir):
        pass
