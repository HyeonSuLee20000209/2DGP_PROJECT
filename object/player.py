import pico2d
import game_framework
import game_world
import state.play_state

import object.ground


PIXEL_PER_METER = 10.0 / 0.25
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 15

size = 15


class IDLE:
    @staticmethod
    def enter(player, event):
        player.dir = 0
        pass

    @staticmethod
    def exit(player):
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
        if player.is_fj:
            if player.f_dir > 0:
                player.image.clip_draw(int(player.frame) * 42, 42, 42, 42, player.x, player.y, 30, 30)
            else:
                player.image.clip_composite_draw(int(player.frame) * 42, 42, 42, 42,
                                                 0, 'h', player.x, player.y, 30, 30)
        else:
            player.image.clip_draw(player.frame * 42, 0, 42, 42, player.x, player.y, 30, 30)


class RUN:
    @staticmethod
    def enter(player, event):
        if player.is_revival:
            player.is_revival = False
            if event == RU:
                player.add_event(DIE)
            if event == LU:
                player.add_event(DIE)
        if event == RD:
            player.velocity += RUN_SPEED_PPS
        if event == LD:
            player.velocity -= RUN_SPEED_PPS
        if event == RU:
            player.velocity -= RUN_SPEED_PPS
        if event == LU:
            player.velocity += RUN_SPEED_PPS
        player.dir = pico2d.clamp(-1, player.velocity, 1)
        player.f_dir = player.dir

    @staticmethod
    def exit(player):
        player.x -= player.velocity * game_framework.frame_time
        player.velocity = 0

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        player.x += player.velocity * game_framework.frame_time
        player.x = pico2d.clamp(0 + 20, player.x, 1000 - 20)

    @staticmethod
    def draw(player):
        if player.dir > 0:
            player.image.clip_draw(int(player.frame) * 42, 42, 42, 42, player.x, player.y, 30, 30)
        else:
            player.image.clip_composite_draw(int(player.frame) * 42, 42, 42, 42,
                                             0, 'h', player.x, player.y, 30, 30)


LD, LU, RD, RU, DIE = range(5)
top, bottom, right, left = range(4)
dj, fj = range(2)

key_event_table = {
    (pico2d.SDL_KEYDOWN, pico2d.SDLK_LEFT)    : LD,
    (pico2d.SDL_KEYUP, pico2d.SDLK_LEFT)      : LU,
    (pico2d.SDL_KEYDOWN, pico2d.SDLK_RIGHT)   : RD,
    (pico2d.SDL_KEYUP, pico2d.SDLK_RIGHT)     : RU
}

next_state = {
    IDLE: {LD: RUN, LU: RUN, RD: RUN, RU: RUN},
    RUN:  {LD: IDLE, LU: IDLE, RD: IDLE, RU: IDLE, DIE: IDLE}
}


max_height = 70


class Player:
    image = None
    sound = None

    def __init__(self, x, y):
        if Player.image is None:
            Player.image = pico2d.load_image('resource/Player.png')
        if Player.sound is None:
            Player.sound = pico2d.load_wav('resource/bounce_sound.wav')
            Player.sound.set_volume(32)
        self.x, self.y = x, y
        self.exist = True

        self.dir = 0
        self.velocity = 0
        self.frame = 0
        self.accel = 1
        self.accel_count = 0

        self.crash_check = False
        self.crash_dir = None

        self.event_queue = []
        # 초기 상태 설정, entry action 수행
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

        self.item = None
        self.is_fj = False
        self.f_dir = 1

        self.is_start = True
        self.is_revival = False

        self.origin_y = y

    def set_location(self, x, y):
        self.x, self.y = x, y

    def update(self):
        self.cur_state.do(self)

        if self.crash_check:
            self.jumping()
        else:
            self.gravity()

        if self.y < 0:
            self.die()

        if self.is_fj is True:
            self.f_jump()

        if self.event_queue:        # 만약에 list event_queue 안에 무언가 들어 있으면
            event = self.event_queue.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, key_event):
        self.event_queue.insert(0, key_event)

    def handle_events(self, event):     # event : 키 입력 이벤트
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
            self.is_fj = False
        if self.item is not None:
            if (event.type, event.key) == (pico2d.SDL_KEYDOWN, pico2d.SDLK_SPACE):
                global max_height
                self.accel = 1
                self.accel_count = 0
                if self.item == dj:
                    self.origin_y = self.y
                    self.is_fj = False
                    self.use_item()
                elif self.velocity == 0:
                    if self.item == fj:
                        max_height = 20
                        self.origin_y = self.y
                        self.is_fj = True
                        self.use_item()

    def use_item(self):
        self.crash_check = True
        self.item = None
        self.image = pico2d.load_image('resource/Player.png')

    def get_bb(self):
        return self.x - size, self.y - size, self.x + size, self.y + size

    def jumping(self):
        if self.y - self.origin_y > max_height:
            self.y = self.origin_y + max_height
            self.crash_check = False
        self.y += RUN_SPEED_PPS * game_framework.frame_time
        self.accel = 1
        self.accel_count = 0
        self.frame = 1

    def gravity(self):
        self.y -= RUN_SPEED_PPS * game_framework.frame_time * self.accel
        if not self.is_fj:
            self.accel = 1 + 0.02 * self.accel_count
            self.accel_count += 1
        self.frame = 3

    def f_jump(self):
        self.x += self.f_dir * 600 * game_framework.frame_time
        self.x = pico2d.clamp(0 + size, self.x, 1000 - size)

    def set_location(self, x, y):
        self.x, self.y = x, y

    def die(self):
        self.accel = 1
        self.accel_count = 0
        self.item = None
        self.is_fj = False
        self.image = pico2d.load_image('resource/Player.png')
        state.play_state.reset()

    def handle_collision(self, other, group):
        if group == 'p:ground':
            if self.is_fj is True:
                self.x -= self.f_dir * 400 * game_framework.frame_time
                self.is_fj = False
        elif group == 'p:bb':
            if self.is_fj is True:
                self.x -= self.f_dir * 400 * game_framework.frame_time
                self.is_fj = False
        elif group == 'p:e_trap':
            self.die()
            self.item = None
        elif group == 'p:spike':
            self.die()
            self.item = None
        elif group == 'p:dj':
            self.item = dj
            self.image = pico2d.load_image('resource/DPlayer.png')
        elif group == 'p:fj':
            self.item = fj
            self.image = pico2d.load_image('resource/FPlayer.png')
        elif group == 'p:jb':
            pass
        elif group == 'p:star':
            pass

    def handle_collision_dir(self, other, group, dir):
        global max_height

        if dir == top:
            self.crash_check = False
            self.y = other.y - size - object.ground.size

        elif dir == bottom:
            if not group == 'p:spike':
                self.y = other.y + size + object.ground.size
                self.origin_y = other.y + size + object.ground.size

            if group == 'p:ground':
                Player.sound.play()
                max_height = 70
                self.crash_check = True
            elif group == 'p:jb':
                Player.sound.play()
                max_height = 160
                self.crash_check = True
            elif group == 'p:bb':
                Player.sound.play()
                max_height = 70
                self.crash_check = True
            elif group == 'p:bjb':
                Player.sound.play()
                max_height = 160
                self.crash_check = True
        elif dir == right:
            self.x = other.x - size - object.ground.size
            # if group == 'p:ground':
            # elif group == 'p:bb':
            #     self.x = other.x - size - object.ground.size
        elif dir == left:
            self.x = other.x + size + object.ground.size
            # if group == 'p:ground':
            # elif group == 'p:bb':
            #     self.x = other.x + size + object.ground.size
