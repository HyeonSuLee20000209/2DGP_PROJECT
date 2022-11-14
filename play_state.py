import pico2d
from pico2d import *

import game_framework
import title_state

from background import Background

import object.player
from object.player import Player
from object.ground import Ground
from object.e_trap import ETrap
from object.spike import Spike
from object.double_jump import DoubleJump
from object.far_jump import FarJump
from object.star import Star


import game_world

p = None
bg = None

stage = 1

ground = []
e_trap = []
spike = []
dj = []
fj = []
star = []


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            # game_framework.change_state(title_state)
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_s):
            reset()
        else:
            p.handle_events(event)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


def collide_top(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_b < left_a < right_b or left_b < right_a < right_b:
        if bottom_b < top_a < top_b:
            return True

    return False


def enter():
    global p
    p = Player(25 + 50, 25 + 50 * 10)
    game_world.add_object(p, 1)

    global bg
    bg = Background()
    game_world.add_object(bg, 0)

    global ground
    for i in range(5):
        ground.append(Ground(50 * i + 25, 25 + 50 * 8))
    for i in range(3):
        ground.append(Ground(50 * (i + 6) + 25, 25 + 50 * 1))
    for i in range(7):
        ground.append(Ground(25 + 50 * 7, 25 + 50 * (i + 5)))
    game_world.add_all_objects(ground, 2)

    game_world.add_collision_pairs(p, ground, 'p:ground')

    global e_trap
    for i in range(8):
        e_trap.append(ETrap(25, 25 + 50 * i))
    e_trap.append(ETrap(25 + 50 * 5, 25 + 50 * 1))
    e_trap.append(ETrap(25 + 50 * 5, 25 + 50 * 2))
    game_world.add_all_objects(e_trap, 2)

    game_world.add_collision_pairs(p, e_trap, 'p:e_trap')

    global spike
    for i in range(4):
        spike.append(Spike(25 + 50 * (i + 3), 25 + 50 * 0))
        spike.append(Spike(25 + 50 * (i + 3), 25 + 50 * 5))
    game_world.add_all_objects(spike, 2)

    game_world.add_collision_pairs(p, spike, 'p:spike')

    global dj
    dj.append(DoubleJump(25 + 50 * 4, 25 + 50 * 3))
    dj.append(DoubleJump(25 + 50 * 4, 25 + 50 * 6))
    game_world.add_all_objects(dj, 3)
    game_world.add_collision_pairs(p, dj, 'p:dj')

    global fj
    fj.append(FarJump(25 + 50 * 9, 25 + 50 * 3))
    game_world.add_all_objects(fj, 3)

    game_world.add_collision_pairs(p, fj, 'p:fj')

    global star
    star.append(Star(25 + 50 * 18, 25))
    game_world.add_all_objects(star, 4)

    game_world.add_collision_pairs(p, star, 'p:star')


def exit():
    game_world.clear()


left, right, up, down = range(4)


def update():
    for g in ground:
        if collide(p, g):
            p.crash_check = True

    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    for g in ground:
        if collide_top(p, g):
            p.y -= object.player.RUN_SPEED_PPS * game_framework.frame_time
            p.crash_check = False


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()


def pause():
    pass


def resume():
    pass


def reset():
    global stage

    exit()
    if stage == 1:
        stage = 2

    enter()


def stage1():
    pass


def stage2():
    pass
