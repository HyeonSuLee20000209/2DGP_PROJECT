import pico2d
from pico2d import *

import game_framework
import play_state
import title_state

image = None


def enter():
    global image
    # if image is None:
    image = load_image('resource/StageSelect.png')


def exit():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.change_state(title_state)
                case pico2d.SDLK_q:
                    game_framework.quit()
                case pico2d.SDLK_SPACE:
                    game_framework.change_state(play_state)


def draw():
    global image
    clear_canvas()
    image.draw(500, 300, 1000, 600)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass

