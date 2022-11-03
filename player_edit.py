import pico2d
import game_framework


PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KMPH = 20.0
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
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        pass

    @staticmethod
    def draw(player):
        if player.dir == right:
            player.image.clip_draw(int(player.frame) * 42, 0, 42, 42, player.x, player.y)
        else:
            player.image.clip_composite_draw(int(player.frame) * 42, 0, 42, 42,
                                             0, 'h', player.x, player.y, 42, 42)


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
        player.face_dir = player.dir
        player.velocity = 0
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        player.x += player.velocity * game_framework.frame_time
        player.x = pico2d.clamp(0 + 20, player.x, 1000 - 20)

    @staticmethod
    def draw(player):
        if player.dir == right:
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


class Player:
    image = None

    def __init__(self, x, y):
        if Player.image is None:
            self.image = pico2d.load_image('resource/Player.png')

        self.x, self.y = x, y
        self.x1, self.y1 = x - 25, y - 25
        self.x2, self.y2 = x + 25, y + 25
        self.dir = 0
        self.velocity = 0
        self.frame = 0

        self.event_queue = []
        # 초기 상태 설정, entry action 수행
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

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
