import pico2d
import game_world


class DoubleJump:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y

        if DoubleJump.image is None:
            DoubleJump.image = pico2d.load_image('resource/DoubleJump.png')

    def draw(self):
        self.image.draw(self.x, self.y, 50, 50)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def handle_collision(self, other, group):
        if group == 'p:dj':
            game_world.remove_object(self)

    def handle_collision_dir(self, other, group, dir):
        pass
