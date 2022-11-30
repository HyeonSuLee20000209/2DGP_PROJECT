import pico2d
from pico2d import *

import game_framework
import title_state
import pause_state

from background import Background

import object.player
import object.ground

from object.player import Player


import game_world
import server
import stage


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(pause_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            # game_framework.change_state(title_state)
            game_framework.quit()
        else:
            server.p.handle_events(event)


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


top, bottom, right, left = range(4)
start = [0, 0]


def collide_dir(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_b < a.x < right_b:
        if top_a > bottom_b > bottom_a:
            return True, top
        if top_a > top_b > bottom_a:
            return True, bottom
    if bottom_b < a.y < top_b:
        if right_a > left_b > left_a:
            return True, left
        if right_a > right_b > left_a:
            return True, right

    return False


def enter():
    global stage, start
    if server.stage == 1:
        start = [object.ground.size + object.ground.size * 2 * 3,
                 object.ground.size + object.ground.size * 2 * 3]
    elif server.stage == 2:
        start = [object.ground.size * 2 * 0,
                 object.ground.size * 2 * 2]

    server.p = Player(start[0], start[1])
    game_world.add_object(server.p, 1)

    server.bg = Background()
    game_world.add_object(server.bg, 0)

    stage.stage(server.stage)


def exit():
    game_world.clear()


up, bottom, left, right = range(4)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            a.handle_collision(b, group)
            b.handle_collision(a, group)
        if collide_dir(a, b):
            check, dir = collide_dir(a, b)
            a.handle_collision_dir(b, group, dir)
            b.handle_collision_dir(a, group, dir)


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
    exit()
    enter()
    server.p.is_revival = True
