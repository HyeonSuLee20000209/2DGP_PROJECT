import pico2d
from pico2d import *

import game_framework
import title_state

import ground
import electric_trap
import monster
import player


p = None
monster1 = None
running = True
e_trap = None
g = None
background = None
g_num = 7


def enter():
    global p, monster1
    global e_trap, g, running, background

    background = load_image('resource/Background.png')
    p = player.Player()
    monster1 = monster.Monster1()
    e_trap = electric_trap.ElectronicTrap()
    g = [ground.Ground() for i in range(g_num)]
    p.set_location(75, 200 + 20)
    monster1.set_location(225, 125 + 20)
    running = True


def exit():
    global e_trap, g, p
    del e_trap, g, p


def update():
    global p
    is_crash_ground(g_num)
    if p.crash_check:
        p.jump()
    else:
        p.gravity()
    p.update()
    monster1.update()
    update_canvas()


def draw():
    global e_trap, g, p
    clear_canvas()
    draw_world()


def draw_world():
    background.draw(500, 300, 1000, 600)
    for i in range(g_num - 2):
        g[i].set_location(150 * i + 75, 100)
        g[i].draw()
    g[g_num - 2].set_location(50 * 14 + 75, 100)
    g[g_num - 2].draw()
    g[g_num - 1].set_location(50 * 14 + 75, 150)
    g[g_num - 1].draw()
    # e_trap.draw(50 * 8 + 75, 100 + 50)
    p.draw()
    draw_rectangle(p.x1, p.y1, p.x2, p.y2)
    monster1.draw()


def is_crash_ground(n):
    for i in range(n):
        if g[i].x1 < p.x2 and g[i].x2 > p.x1:
            if p.y1 > g[i].y2 > p.y1 - 2:
                p.crash_check = True
                return
        else:
            pass

    if p.y < 0:
        p.set_location(75, 200 + 20)


def is_crash_wall(n):
    p.moving()
    pass


right = 1
left = -1

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
                    p.dir = right
                    is_crash_wall(g_num)
                case pico2d.SDLK_LEFT:
                    p.dir = left
                    is_crash_wall(g_num)
                case pico2d.SDLK_SPACE:
                    pass
        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_RIGHT:
                    p.move -= 1
                case pico2d.SDLK_LEFT:
                    p.move += 1
