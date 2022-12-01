import pico2d
import game_world

top, bottom, right, left = range(4)


class BrokenBlock:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.exist = True

        if BrokenBlock.image is None:
            BrokenBlock.image = pico2d.load_image('resource/Broken_Block.png')

    def draw(self):
        self.image.draw(self.x, self.y, 50, 50)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def handle_collision(self, other, group):
        pass

    def handle_collision_dir(self, other, group, dir):
        if dir == bottom:
            if group == 'p:bb':
                self.exist = False
