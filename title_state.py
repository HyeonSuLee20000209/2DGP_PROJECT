from pico2d import *

import game_framework
import play_state
import select_state


image = True

start = None
start_color = 0

finish = None
finish_color = 0


def enter():
    global image, start, finish
    image = load_image('resource/Title.png')
    start = load_font('resource/ENCR10B.TTF', 50)
    finish = load_font('resource/ENCR10B.TTF', 50)


def exit():
    global image, start, finish
    del image, start, finish


def handle_events():
    global image
    global start, start_color
    global finish, finish_color

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                case pico2d.SDLK_q:
                    game_framework.quit()
                case pico2d.SDLK_SPACE:
                    game_framework.change_state(play_state)
        elif event.type == SDL_MOUSEMOTION:
            if 0 < event.x < 109 * 1000 // image.w:
                if 67 * 600 // image.h < event.y < 99 * 600 // image.h:
                    start_color = 125
                elif 112 * 600 // image.h < event.y < 142 * 600 // image.h:
                    finish_color = 125
                else:
                    start_color, finish_color = 0, 0
            else:
                start_color, finish_color = 0, 0
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == 1:
                if 0 < event.x < 109 * 1000 // image.w:
                    if 67 * 600 // image.h < event.y < 99 * 600 // image.h:
                        game_framework.change_state(select_state)
                        start_color, finish_color = 0, 0
                    elif 112 * 600 // image.h < event.y < 142 * 600 // image.h:
                        game_framework.quit()


def draw():
    global image, start, finish
    clear_canvas()
    image.draw(500, 300, 1000, 600)
    start.draw(10, 112 * 600 // image.h, 'Game Start', (start_color, start_color, start_color))
    finish.draw(75, 67 * 600 // image.h, 'Close', (finish_color, finish_color, finish_color))
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
