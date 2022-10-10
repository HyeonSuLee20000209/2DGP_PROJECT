from pico2d import *


class ElectronicTrap:
    def __init__(self):
        self.image = load_image('Electronic_Trap.png')
        self.x, self.y = 0, 0

    def draw(self):
        self.x, self.y = 400, 300
        self.image.draw(self.x, self.y)


class Ground:
    def __init__(self):
        self.image = load_image('Ground.png')
        self.x, self.y = 0, 0

    def draw(self, x, y):
        self.x, self.y = x, y
        self.image.draw(self.x, self.y)


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE or event.key == SDLK_q:
                running = False
            # 캐릭터 이동
            if event.key == SDLK_w:
                pass
            if event.key == SDLK_a:
                pass
            if event.key == SDLK_s:
                pass
            if event.key == SDLK_d:
                pass


running = True
e_trap = None
ground = None


def enter():
    global e_trap, ground, running
    e_trap = ElectronicTrap()
    ground = Ground()
    running = True


# finalization code
def end():
    global e_trap, ground
    del e_trap, ground


def update():
    pass


def draw():
    global e_trap, ground
    clear_canvas()
    e_trap.draw()
    ground.draw(20, 200)
    update_canvas()
