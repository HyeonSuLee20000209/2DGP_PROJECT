import pico2d
from pico2d import *

import game_framework
import title_state
import math


class Ground:
    def __init__(self):
        self.image = load_image('Ground.png')
        self.x, self.y = 0, 0

    def draw(self, x, y):
        self.x, self.y = x, y
        self.image.draw(self.x, self.y)


class ElectronicTrap:
    def __init__(self):
        self.image = load_image('Electronic_Trap.png')
        self.x, self.y = 0, 0

    def draw(self, x, y):
        self.x, self.y = x, y
        self.image.draw(self.x, self.y)


right = 1
left = -1


class Player:
    def __init__(self):
        self.x, self.y = 0, 0
        self.move = 0
        self.dir = right
        self.frame = 0
        self.count = 0
        self.image = load_image('Player.png')

    def update(self):
        if self.count < 5:
            self.y += 20
        elif self.count < 10:
            self.y -= 20

        self.count += 1
        if self.count == 1:
            self.frame = 1
        elif self.count == 5:
            self.frame = 2
        elif self.count == 6:
            self.frame = 3
        elif self.count == 10:
            self.frame = 0
            self.count = 0
        delay(0.075)

    def set_location(self, x, y):
        self.x, self.y = x, y

    def draw(self):
        if self.dir == right:
            self.image.clip_draw(self.frame * 42, 0, 42, 42, self.x, self.y)
        elif self.dir == left:
            self.image.clip_composite_draw(self.frame * 42, 0, 42, 42, 0, 'h', self.x, self.y, 42, 42)

    def reset_count(self):
        self.count = 0


player = None
running = True
e_trap = None
ground = None
background = None


def enter():
    global player, e_trap, ground, running, background
    background = load_image('Background.png')
    player = Player()
    e_trap = ElectronicTrap()
    ground = Ground()
    player.set_location(75, 125 + 20)
    running = True


def exit():
    global e_trap, ground, player
    del e_trap, ground, player


def update():
    global player
    player.update()


def draw():
    global e_trap, ground, player
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    background.draw_now(500, 300, 1000, 600)
    for i in range(18):
        ground.draw(50 * i + 75, 100)
    e_trap.draw(50 * 8 + 75, 100 + 50)
    player.draw()


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.change_state(title_state)
                case pico2d.SDLK_q:
                    game_framework.change_state(title_state)
                # 캐릭터 이동
                case pico2d.SDLK_RIGHT:
                    player.dir = right
                    player.move += 15
                case pico2d.SDLK_LEFT:
                    player.dir = left
                    player.move -= 15
                case pico2d.SDLK_SPACE:
                    pass
        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_RIGHT:
                    player.move -= 15
                case pico2d.SDLK_LEFT:
                    player.move += 15
