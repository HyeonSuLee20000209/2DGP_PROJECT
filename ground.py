import pico2d


class Ground:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y

        if Ground.image is None:
            Ground.image = pico2d.load_image('resource/Ground.png')

    def draw(self):
        self.image.draw(self.x, self.y)
        pico2d.draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def handle_collision(self, other, group):
        pass
