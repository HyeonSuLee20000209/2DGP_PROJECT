import pico2d
import game_world
import game_framework
import state.select_state
import server
import stage


class Star:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.exist = True

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
            self.exist = False
            stage.s[server.stage] = True
            game_framework.change_state(state.select_state)

    def handle_collision_dir(self, other, group, dir):
        pass
