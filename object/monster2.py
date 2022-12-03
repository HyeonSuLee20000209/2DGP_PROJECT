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


class Monster2:
    def __init__(self, x, y):
        self.image = pico2d.load_image('resource/Monster2.png')
        self.x, self.y = x, y - 5
        self.frame = 1
        self.timer = 0
        self.accel = 1
        self.accel_count = 0
        self.velocity = 0
        self.exist = True

    def update(self):
        self.timer += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        self.activate()
        self.moving()

    def activate(self):
        if self.timer > 25:
            self.frame = 2
        if self.timer > 40:
            self.frame = 0

    def moving(self):
        if self.frame == 2:
            self.y += RUN_SPEED_PPS * game_framework.frame_time
        if self.frame == 0:
            self.y -= RUN_SPEED_PPS * game_framework.frame_time * self.accel
            self.accel = 1 + 0.04 * self.accel_count
            self.accel_count += 1

    def draw(self):
        self.image.clip_draw(self.frame * 31, 0, 31, 42, self.x, self.y)

    def get_bb(self):
        return self.x - 15, self.y - 20, self.x + 15, self.y + 20

    def handle_collision(self, other, group):
        pass

    def handle_collision_dir(self, other, group, dir):
        if dir == bottom:
            if group == 'g:m2':
                self.y = other.y + 20 + object.ground.size
                self.timer = 0
                self.accel = 1
                self.accel_count = 0
                self.frame = 1
            if group == 'bb:m2' and other.exist:
                self.y = other.y + 20 + object.ground.size
                self.timer = 0
                self.accel = 1
                self.accel_count = 0
                self.frame = 1
