from pico2d import *

import game_framework
import state.title_state
import state.pause_state

from object.background import Background

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
            game_framework.push_state(state.pause_state)
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
    global start
    if server.stage == 0:
        start = [object.ground.size + object.ground.size * 2 * 2,
                 object.ground.size + object.ground.size * 2 * 7]
    elif server.stage == 1:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 4]
    elif server.stage == 2:
        start = [object.ground.size + object.ground.size * 2 * 18,
                 object.ground.size + object.ground.size * 2 * 11]
    elif server.stage == 3:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 10]
    elif server.stage == 4:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 4]
    elif server.stage == 5:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 4]
    elif server.stage == 6:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 4]
    elif server.stage == 7:
        start = [object.ground.size + object.ground.size * 2 * 1,
                 object.ground.size + object.ground.size * 2 * 4]
    elif server.stage == 8:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 4]
    elif server.stage == 9:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 4]
    elif server.stage == 10:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 4]
    elif server.stage == 11:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 4]
    elif server.stage == 12:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 4]
    elif server.stage == 13:
        start = [object.ground.size + object.ground.size * 2 * 2,
                 object.ground.size + object.ground.size * 2 * 10]
    elif server.stage == 14:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 4]
    elif server.stage == 15:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 4]
    elif server.stage == 16:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 4]
    elif server.stage == 17:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 4]
    elif server.stage == 18:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 4]
    elif server.stage == 19:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 4]
    elif server.stage == 20:
        start = [object.ground.size + object.ground.size * 2 * 0,
                 object.ground.size + object.ground.size * 2 * 4]

    server.p = Player(start[0], start[1])
    game_world.add_object(server.p, 1)

    server.bg = Background()
    server.bg.bgm.repeat_play()

    game_world.add_object(server.bg, 0)

    stage.stage(server.stage)


def exit():
    server.bg.bgm.stop()
    server.clear()
    game_world.clear()


up, bottom, left, right = range(4)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b) and b.exist:
            a.handle_collision(b, group)
            b.handle_collision(a, group)
        if collide_dir(a, b) and b.exist:
            check, dir = collide_dir(a, b)
            a.handle_collision_dir(b, group, dir)
            b.handle_collision_dir(a, group, dir)


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    for game_object in game_world.all_objects():
        if game_object.exist:
            game_object.draw()


def pause():
    pass


def resume():
    pass


def reset():
    server.p.set_location(start[0], start[1])
    server.p.is_revival = True
    for game_object in game_world.all_objects():
        if not game_object.exist:
            game_object.exist = True
    server.star_count = len(server.star)
