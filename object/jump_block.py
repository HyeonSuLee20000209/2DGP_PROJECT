import pico2d


class JumpBlock:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y

        if JumpBlock.image is None:
            JumpBlock.image = pico2d.load_image('resource/JumpBlock.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def handle_collision(self, other, group):
        pass

    def handle_collision_bottom(self, other, group):
        pass
