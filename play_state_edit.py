import pico2d
from pico2d import *

import game_framework
import title_state


import player_edit


p = None
bg = None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            game_framework.change_state(title_state)
        else:
            p.handle_events(event)


def enter():
    global p, bg

    p = player_edit.Player()
    bg = load_image('resource/Background.png')
    pass


def exit():
    global p, bg
    del p
    del bg


def update():
    p.update()
    pass


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    bg.draw(500, 300, 1000, 600)
    p.draw()


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
