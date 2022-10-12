from pico2d import *


class Player:
    def __init__(self):
        self.image = load_image()

class ElectronicTrap:
    def __init__(self):
        self.image = load_image('Electronic_Trap.png')

    def draw(self, x, y):
        self.image.draw(x, y)


class Ground:
    def __init__(self):
        self.image = load_image('Ground.png')

    def draw(self, x, y):
        self.image.draw(x, y)


def handle_events():
    global running

    key_events = get_events()
    for event in key_events:
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
    ground = [Ground() for i in range(20)]
    running = True


# finalization code
def end():
    global e_trap, ground
    del e_trap, ground


def update():
    pass


def draw():
    # e_trap.draw(20, 20)

    global e_trap, ground
    clear_canvas()
    background = pico2d.load_image('background.png')
    background.draw_now(500, 300, 1000, 600)
    for i in range(18):
        ground[i].draw(50 * i + 75, 100)
    update_canvas()


pico2d.open_canvas(1000, 600)

enter()
draw()

while running:
    handle_events()


end()
