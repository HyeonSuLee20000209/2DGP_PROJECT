from pico2d import *


class ElectronicTrap:
    def __init__(self):
        self.image = load_image('Electronic_Trap.png')
        self.x, self.y = 0, 0

    def draw(self, x, y):
        self.x, self.y = x, y
        self.image.draw(self.x, self.y)


open_canvas(1000, 700)
electronic = ElectronicTrap()


def update():
    clear_canvas()
    electronic.draw(25, 25)
    update_canvas()

    delay(0.05)


def handle_events():
    global running

    what_events = get_events()
    for event in what_events:
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

while running:
    update()

    handle_events()

close_canvas()
