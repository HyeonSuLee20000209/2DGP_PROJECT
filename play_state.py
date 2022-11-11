import pico2d
from pico2d import *

import game_framework
import title_state

import player
from player import Player
from background import Background
from ground import Ground
from e_trap import ETrap
from double_jump import DoubleJump

import game_world

p = None
bg = None
ground = []
g_num = 10
e_trap = []
dj = []

dj_list = {
    (0 + 25 + 50 * 2, 50 * 6), (0 + 25 + 50 * 9, 50 * 6)
}


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
    p = Player(75, 150 + 20)
    game_world.add_object(p, 1)

    global bg
    bg = Background()
    game_world.add_object(bg, 0)

    global ground
    for i in range(g_num):
        ground.append(Ground(50 * i + 25, 50))
    for i in range(5):
        ground.append(Ground(0 + 25, 50 * (i + 1)))
    ground.append(Ground(0 + 25 + 50 * 3, 50 * 3))
    ground.append(Ground(0 + 25 + 50 * 2, 50 * 2))
    game_world.add_all_objects(ground, 2)

    global e_trap
    e_trap.append(ETrap(500 + 25, 50))
    game_world.add_all_objects(e_trap, 2)

    global dj
    for x, y in dj_list:
        dj.append(DoubleJump(x, y))
    game_world.add_all_objects(dj, 3)

    game_world.add_collision_pairs(p, ground, 'p:ground')
    game_world.add_collision_pairs(p, e_trap, 'p:e_trap')
    game_world.add_collision_pairs(p, dj, 'p:dj')


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
            p.y -= player.RUN_SPEED_PPS * game_framework.frame_time
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
    game_world.layer_clear(3)
    for x, y in dj_list:
        dj.append(DoubleJump(x, y))
    game_world.add_all_objects(dj, 3)
    game_world.add_collision_pairs(p, dj, 'p:dj')
