import pico2d
from pico2d import *

import game_framework
import title_state

from player_edit import Player
from background import Background
from ground import Ground

import game_world

player = None
bg = None
ground = []
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
            player.handle_events(event)


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


def enter():
    global player
    player = Player(75, 200 + 20)
    game_world.add_object(player, 2)

    global bg
    bg = Background()
    game_world.add_object(bg, 0)

    global ground
    for i in range(g_num):
        ground.append(Ground(50 * i + 25, 50))
    game_world.add_all_objects(ground, 1)
    pass


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for g in ground:
        if collide(player, g):
            player.crash_check = True

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
