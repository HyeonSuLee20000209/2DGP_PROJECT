import pico2d
from pico2d import *

import game_framework
import title_state

from player_edit import Player
from background import Background
from ground import Ground

import game_world

p = None
bg = None
g = []
g_num = 10


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


def enter():
    global p, bg, g
    p = Player(75, 200 + 20)
    bg = Background()
    for i in range(g_num):
        g.append(Ground(50 * i + 25, 50))
    game_world.add_object(bg, 0)
    game_world.add_all_objects(g, 1)
    game_world.add_object(p, 2)
    pass


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()


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


def pause():
    pass


def resume():
    pass
