import pico2d
import game_framework
import state.play_state

import object.ground

PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KMPH = 15.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

top, bottom, right, left = range(4)

size = 20


class Monster1:
    def __init__(self, x, y):
        self.image = pico2d.load_image('resource/Monster1.png')
        self.x, self.y = x, y - 5
        self.frame = [0, 1, 2, 3, 4, 3, 2, 1]
        self.what_frame = 0
        self.count = 0
        self.dir = right
        self.velocity = 0
        self.exist = True

    def update(self):
        self.what_frame = (self.what_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        if self.dir == right:
            self.velocity = RUN_SPEED_PPS
        else:
            self.velocity = -RUN_SPEED_PPS

        self.x += self.velocity * game_framework.frame_time

    def draw(self):
        if self.dir == right:
            self.image.clip_draw(self.frame[int(self.what_frame)] * 42, 42, 42, 42, self.x, self.y, size * 2, size * 2)
        elif self.dir == left:
            self.image.clip_composite_draw(self.frame[int(self.what_frame)] * 42, 42, 42, 42,
                                           0, 'h', self.x, self.y,  size * 2, size * 2)

    def get_bb(self):
        return self.x - size, self.y - size, self.x + size, self.y + size

    def handle_collision(self, other, group):
        pass

    def handle_collision_dir(self, other, group, dir):
        if group == 'g:m1':
            if dir == left:
                self.dir = left
                self.x = other.x - size - object.ground.size
            elif dir == right:
                self.dir = right
                self.x = other.x + size + object.ground.size
