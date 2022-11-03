import pico2d


class Ground:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.x1, self.y1 = x - 25, y - 25
        self.x2, self.y2 = x + 25, y + 25

        if Ground.image is None:
            Ground.image = pico2d.load_image('resource/Ground.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
