from pico2d import *

import game_framework
import play_state
import select_state

c = None
e = None

white, gray = range(2)

c_color = white
e_color = white

def enter():
    global c, e
    c = load_image('resource/White_Continue.png')
    e = load_image('resource/White_Exit.png')


def exit():
    global c, e
    del c, e


def update():
    pass


def draw():
    global c, e
    clear_canvas()
    play_state.draw_world()
    if c_color is white:
        c = load_image('resource/White_Continue.png')
    else:
        c = load_image('resource/Gray_Continue.png')
    if e_color is white:
        e = load_image('resource/White_Exit.png')
    else:
        e = load_image('resource/Gray_Exit.png')

    c.draw(500, 300)
    e.draw(500, 300)
    update_canvas()


def handle_events():
    global c, e
    global c_color, e_color

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
        elif event.type == SDL_MOUSEMOTION:
            if 200 < event.x < 800:
                if 100 < event.y < 250:
                    c_color = gray
                elif 350 < event.y < 500:
                    e_color = gray
                else:
                    c_color, e_color = white, white
            else:
                c_color, e_color = white, white
        if event.type == SDL_MOUSEBUTTONDOWN:
            if 200 < event.x < 800:
                if 100 < event.y < 250:
                    game_framework.pop_state()
                elif 350 < event.y < 500:
                    game_framework.pop_state()
                    game_framework.change_state(select_state)
                else:
                    game_framework.pop_state()
            else:
                game_framework.pop_state()