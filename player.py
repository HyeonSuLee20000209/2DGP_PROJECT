import pico2d
import game_framework
import game_world
import play_state


PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


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
        player.image.clip_draw(player.frame * 42, 0, 42, 42, player.x, player.y)


class RUN:
    @staticmethod
    def enter(player, event):
        if event == RD:
            player.velocity += RUN_SPEED_PPS
        if event == LD:
            player.velocity -= RUN_SPEED_PPS
        if event == RU:
            player.velocity -= RUN_SPEED_PPS
        if event == LU:
            player.velocity += RUN_SPEED_PPS
        player.dir = pico2d.clamp(-1, player.velocity, 1)

    @staticmethod
    def exit(player):
        player.x -= player.velocity * game_framework.frame_time
        player.velocity = 0
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        player.x += player.velocity * game_framework.frame_time
        player.x = pico2d.clamp(0 + 20, player.x, 1000 - 20)

    @staticmethod
    def draw(player):
        if player.dir > 0:
            player.image.clip_draw(int(player.frame) * 42, 42, 42, 42, player.x, player.y)
        else:
            player.image.clip_composite_draw(int(player.frame) * 42, 42, 42, 42,
                                             0, 'h', player.x, player.y, 42, 42)


LD, LU, RD, RU = range(4)
left, right = range(2)

key_event_table = {
    (pico2d.SDL_KEYDOWN, pico2d.SDLK_LEFT)    : LD,
    (pico2d.SDL_KEYUP, pico2d.SDLK_LEFT)      : LU,
    (pico2d.SDL_KEYDOWN, pico2d.SDLK_RIGHT)   : RD,
    (pico2d.SDL_KEYUP, pico2d.SDLK_RIGHT)     : RU
}

next_state = {
    IDLE: {LD: RUN, LU: RUN, RD: RUN, RU: RUN},
    RUN:  {LD: IDLE, LU: IDLE, RD: IDLE, RU: IDLE}
}


dj, fj = range(2)

class Player:
    image = None

    def __init__(self, x, y):
        if Player.image is None:
            self.image = pico2d.load_image('resource/Player.png')

        self.x, self.y = x, y
        self.start = [75, 150 + 20]

        self.dir = 0
        self.velocity = 0
        self.frame = 0

        self.crash_check = False
        self.crash_dir = None

        self.is_jump = True
        self.jump_count = 0

        self.event_queue = []
        # 초기 상태 설정, entry action 수행
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

        self.item = None

    def update(self):
        self.cur_state.do(self)

        if self.crash_check:
            self.jump()
        else:
            self.gravity()

        if self.y < 0:
            self.die()

        if self.event_queue:        # 만약에 list event_queue 안에 무언가 들어 있으면
            event = self.event_queue.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        pico2d.draw_rectangle(*self.get_bb())

    def add_event(self, key_event):
        self.event_queue.insert(0, key_event)

    def handle_events(self, event):     # event : 키 입력 이벤트
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        if self.item == dj:
            if (event.type, event.key) == (pico2d.SDL_KEYDOWN, pico2d.SDLK_SPACE):
                self.jump_count = 0
                self.crash_check = True
                self.item = None
                self.image = pico2d.load_image('resource/Player.png')

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def jump(self):
        self.y += RUN_SPEED_PPS * game_framework.frame_time
        self.frame = 1

        self.jump_count += 1

        if self.jump_count % 100 == 0:
            self.crash_check = False

    def gravity(self):
        self.jump_count = 0

        self.y -= RUN_SPEED_PPS * game_framework.frame_time
        self.frame = 3

    def set_location(self, x, y):
        self.x, self.y = x, y

    def die(self):
        self.x, self.y = self.start[0], self.start[1]
        play_state.reset()

    def handle_collision(self, other, group):
        if group == 'p:ground':
            self.x -= self.velocity * game_framework.frame_time
        elif group == 'p:e_trap':
            self.die()
            self.item = None
        elif group == 'p:dj':
            self.item = dj
            self.image = pico2d.load_image('resource/DPlayer.png')
            pass
