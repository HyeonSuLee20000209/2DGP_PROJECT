from pico2d import *
import game_world
import game_framework
import state.select_state
import server
import stage


class Star:
    image = None
    eat_sound = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.exist = True

        if Star.image is None:
            Star.image = pico2d.load_image('resource/Star.png')
        if Star.eat_sound is None:
            Star.eat_sound = load_wav('resource/collect_star.wav')
            Star.eat_sound.set_volume(32)

    def draw(self):
        self.image.draw(self.x, self.y, 40, 40)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        if group == 'p:star':
            self.exist = False
            Star.eat_sound.play()
            server.star_count -= 1
            if server.star_count == 0:
                stage.s[server.stage] = True
                game_framework.change_state(state.select_state)

    def handle_collision_dir(self, other, group, dir):
        pass
