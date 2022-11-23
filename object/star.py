import pico2d
import game_world
import game_framework
import title_state
import play_state


class Star:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y

        if Star.image is None:
            Star.image = pico2d.load_image('resource/Star.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def handle_collision(self, other, group):
        if group == 'p:star':
            game_world.remove_object(self)
            play_state.exit()
            play_state.stage += 1
            play_state.enter()

    def handle_collision_bottom(self, other, group):
        pass
