import pico2d
from pico2d import *

import game_framework
import title_state
import math


class Ground:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.x1, self.y1 = 0, 0
        self.x2, self.y2 = 0, 0
        if Ground.image == None:
            Ground.image = load_image('Ground.png')

    def set_location(self, x, y):
        self.x, self.y = x, y
        self.x1, self.y1 = x - 25, y - 25
        self.x2, self.y2 = x + 25, y + 25

    def draw(self):
        self.image.draw(self.x, self.y)


class ElectronicTrap:
    def __init__(self):
        self.image = load_image('Electronic_Trap.png')
        self.x, self.y = 0, 0
        self.x1, self.y1 = 0, 0
        self.x2, self.y2 = 0, 0

    def set_location(self, x, y):
        self.x, self.y = x, y
        self.x1, self.y1 = x - 25, y - 25
        self.x2, self.y2 = x + 25, y + 25

    def draw(self, x, y):
        self.x, self.y = x, y
        self.image.draw(self.x, self.y)


right = 1
left = -1


class Monster1:
    def __init__(self):
        self.image = load_image('monster1.png')
        self.x, self.y = 0, 0
        self.x1, self.y1 = 0, 0
        self.x2, self.y2 = 0, 0
        self.frame = 0
        self.count = 0
        self.dir = right

    def set_location(self, x, y):
        self.x, self.y = x, y
        self.x1, self.y1 = x - 20, y - 20
        self.x2, self.y2 = x + 20, y + 20

    def update(self):
        self.count += 1
        if self.x > 1000:
            self.dir = left
        elif self.x < 0:
            self.dir = right

        if self.dir == right:
            self.x += 0.5
        else:
            self.x -= 0.5

        if self.count % 50 == 0:
            monster1.frame = (monster1.frame + 1) % 5

        self.x1, self.y1 = self.x - 20, self.y - 20
        self.x2, self.y2 = self.x + 20, self.y + 20

    def draw(self):
        if self.dir == right:
            self.image.clip_draw(self.frame * 42, 42, 42, 42, self.x, self.y)
        elif self.dir == left:
            self.image.clip_composite_draw(self.frame * 42, 42, 42, 42, 0, 'h', self.x, self.y, 42, 42)


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
        self.image = load_image('Player.png')

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
            player.move += 1
        elif self.dir == left:
            player.move -= 1

    def set_location(self, x, y):
        self.x, self.y = x, y
        self.x1, self.y1 = x - 10, y - 10
        self.x1, self.y2 = x + 10, y + 10

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
        self.x1, self.y1 = self.x - 10, self.y - 10
        self.x2, self.y2 = self.x + 10, self.y + 10
        pass


player = None
monster1 = None
running = True
e_trap = None
ground = None
background = None
g_num = 16


def enter():
    global player, monster1
    global e_trap, ground, running, background

    background = load_image('Background.png')
    player = Player()
    monster1 = Monster1()
    e_trap = ElectronicTrap()
    ground = [Ground() for i in range(g_num)]
    player.set_location(75, 250 + 20)
    monster1.set_location(225, 125 + 20)
    running = True


def exit():
    global e_trap, ground, player
    del e_trap, ground, player


def update():
    global player
    is_crash_ground(g_num)
    if player.crash_check:
        player.jump()
    else:
        player.gravity()
    player.update()
    monster1.update()
    update_canvas()
    delay(0.001)


def draw():
    global e_trap, ground, player
    clear_canvas()
    draw_world()


def draw_world():
    background.draw(500, 300, 1000, 600)
    for i in range(g_num - 2):
        ground[i].set_location(50 * i + 75, 100)
        ground[i].draw()
    ground[g_num - 2].set_location(50 * 14 + 75, 150)
    ground[g_num - 2].draw()
    ground[g_num - 1].set_location(50 * 14 + 75, 200)
    ground[g_num - 1].draw()
    # e_trap.draw(50 * 8 + 75, 100 + 50)
    player.draw()
    monster1.draw()


def is_crash_ground(n):
    for i in range(n):
        if ground[i].x1 < player.x2 and ground[i].x2 > player.x1:
            if player.y1 > ground[i].y2 > player.y1 - 2:
                player.crash_check = True
        elif player.y < 0:
            player.set_location(75, 250 + 20)
        else:
            pass


def is_crash_wall(n):
    player.moving()
    pass


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
                    is_crash_wall(g_num)
                case pico2d.SDLK_LEFT:
                    player.dir = left
                    is_crash_wall(g_num)
                case pico2d.SDLK_SPACE:
                    pass
        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_RIGHT:
                    player.move -= 1
                case pico2d.SDLK_LEFT:
                    player.move += 1
