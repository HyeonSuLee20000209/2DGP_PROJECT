import pico2d


class ETrap:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y

        if ETrap.image is None:
            ETrap.image = pico2d.load_image('resource/Electronic_Trap.png')

    def draw(self):
        self.image.draw(self.x, self.y)
        pico2d.draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def handle_collision(self, other, group):
        pass
