import pico2d
import play_state


class IDLE:
    @staticmethod
    def enter():
        print('enter idle')
        pass

    @staticmethod
    def exit():
        print('exit idle')
        pass

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass


class RUN:
    @staticmethod
    def enter():
        print('enter run')
        pass

    @staticmethod
    def exit():
        print('exit run')
        pass

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass


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
    def __init__(self):
        self.x, self.y = 0, 0
        self.x1, self.y1 = 0, 0
        self.x2, self.y2 = 0, 0
        self.move = 0
        self.dir = right
        self.frame = 0
        self.count = 0
        self.crash_check = False
        self.image = pico2d.load_image('resource/Player.png')

    def jump(self):
        self.y += 1
        self.count += 1

        if self.count == 1:
            self.frame = 1
        elif self.count == 100:
            self.frame = 2
            self.count = 0
            self.crash_check = False

    def gravity(self):
        self.frame = 3
        self.y -= 1

    def moving(self):
        if self.dir == right:
            self.move += 1
        elif self.dir == left:
            self.move -= 1

    def set_location(self, x, y):
        self.x, self.y = x, y
        self.x1, self.y1 = x - 20, y - 20
        self.x1, self.y2 = x + 20, y + 20

    def draw(self):
        if self.move > 0:
            self.dir = right
        elif self.move < 0:
            self.dir = left

        if self.dir == right:
            self.image.clip_draw(self.frame * 42, 0, 42, 42, self.x, self.y)
        elif self.dir == left:
            self.image.clip_composite_draw(self.frame * 42, 0, 42, 42, 0, 'h', self.x, self.y, 42, 42)

    def update(self):
        self.x1, self.y1 = self.x - 20, self.y - 20
        self.x2, self.y2 = self.x + 20, self.y + 20
