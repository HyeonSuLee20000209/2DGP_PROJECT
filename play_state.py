import pico2d
from pico2d import *

import game_framework
import title_state

import ground
import electric_trap
import monster
import player


p = None
m1 = None
running = True
e_trap = None
g_list = None
background = None
g_num = 7


def enter():
    global p, m1
    global e_trap, g_list, running, background

    background = load_image('resource/Background.png')
    p = player.Player()
    m1 = monster.Monster1()
    e_trap = electric_trap.ElectronicTrap()
    g_list = [ground.Ground() for i in range(g_num)]
    p.set_location(75, 200 + 20)
    m1.set_location(225, 125 + 20)
    running = True


def exit():
    global e_trap, g_list, p, m1
    del e_trap, g_list, p, m1


def update():
    global p, m1
    is_crash_ground(g_num)
    if p.crash_check:
        p.jump()
    else:
        p.gravity()
    p.update()
    m1.update()

    for g in g_list:
        if is_crash(p, g):
            if p.dir == right:
                p.x -= 2 * p.move
            else:
                p.x += 2 * p.move
            break

    if is_crash(p, m1):
        pass

    p.x += p.move
    update_canvas()


def draw():
    global e_trap, g_list, p
    clear_canvas()
    draw_world()


def draw_world():
    background.draw(500, 300, 1000, 600)
    for i in range(g_num - 2):
        g_list[i].set_location(150 * i + 75, 100)
        g_list[i].draw()
    g_list[g_num - 2].set_location(50 * 14 + 75, 150)
    g_list[g_num - 2].draw()
    g_list[g_num - 1].set_location(50 * 14 + 75, 200)
    g_list[g_num - 1].draw()
    # e_trap.draw(50 * 8 + 75, 100 + 50)
    p.draw()
    m1.draw()

    # 충돌 박스 그리기
    draw_rectangle(p.x1, p.y1, p.x2, p.y2)
    draw_rectangle(m1.x1, m1.y1, m1.x2, m1.y2)


def is_crash_ground(n):
    for g in g_list:
        if g.x1 < p.x2 and g.x2 > p.x1:
            if p.y1 > g.y2 > p.y1 - 2:
                p.crash_check = True
                return
        else:
            pass

    if p.y < 0:
        p.set_location(75, 200 + 20)


right = 1
left = -1


def is_crash(a, b):
    if a.x1 > b.x2:
        return False
    if a.x2 < b.x1:
        return False
    if a.y1 > b.y2:
        return False
    if a.y2 < b.y1:
        return False

    return True


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
                    p.moving()
                case pico2d.SDLK_LEFT:
                    p.dir = left
                    p.moving()
                case pico2d.SDLK_SPACE:
                    pass
        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_RIGHT:
                    p.move -= 1
                case pico2d.SDLK_LEFT:
                    p.move += 1
