import pico2d


class IDLE:
    @staticmethod
    def enter(player, event):
        print('enter idle')
        player.dir = 0
        pass

    @staticmethod
    def exit(player):
        print('exit idle')
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 4
        pass

    @staticmethod
    def draw(player):
        if player.face_dir == right:
            player.image.clip_draw(player.frame * 42, 0, 42, 42, player.x, player.y + 20)
        else:
            player.image.clip_composite_draw(player.frame * 42, 0, 42, 42, 0, 'h', player.x, player.y + 20, 42, 42)
        pass


class RUN:
    @staticmethod
    def enter(player, event):
        print('enter run')
        if event == RD:
            player.dir += 1
            player.face_dir = right
        if event == LD:
            player.dir -= 1
            player.face_dir = left
        if event == RU:
            player.dir -= 1
        if event == LU:
            player.dir += 1
        pass

    @staticmethod
    def exit(player):
        print('exit run')
        player.face_dir = player.dir
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 4
        player.x += player.dir
        player.x = pico2d.clamp(0, player.x, 1000)
        pass

    @staticmethod
    def draw(player):
        if player.face_dir == right:
            player.image.clip_draw(player.frame * 42, 42, 42, 42, player.x, player.y + 20)
        else:
            player.image.clip_composite_draw(player.frame * 42, 42, 42, 42, 0, 'h', player.x, player.y + 20, 42, 42)
        pass


LD, LU, RD, RU, JP = range(5)
left, right = range(2)

key_event_table = {
    (pico2d.SDL_KEYDOWN, pico2d.SDLK_LEFT)    : LD,
    (pico2d.SDL_KEYUP, pico2d.SDLK_LEFT)      : LU,
    (pico2d.SDL_KEYDOWN, pico2d.SDLK_RIGHT)   : RD,
    (pico2d.SDL_KEYUP, pico2d.SDLK_RIGHT)     : RU,
    (pico2d.SDL_KEYUP, pico2d.SDLK_SPACE)     : JP
}

next_state = {
    IDLE: {LD: RUN, LU: RUN, RD: RUN, RU: RUN},
    RUN:  {LD: IDLE, LU: IDLE, RD: IDLE, RU: IDLE}
}


class Player:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.frame = 0
        self.dir = 0
        self.face_dir = right

        self.image = pico2d.load_image('resource/Player.png')

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

    def handle_events(self, event): # event : 키 입력 이벤트
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    # 기타 다른 함수
    def set_location(self, x, y):
        pass
