import pico2d
from pico2d import *

import game_framework
import state.play_state
import state.title_state

import server

image = None
clear = None

top = [130, 260, 390]
bottom = [225, 355, 485]
left = [50, 180, 310, 440, 570, 700, 830]
right = [150, 280, 410, 540, 670, 800, 930]


def enter():
    global image, clear
    # if image is None:
    image = load_image('resource/StageSelect.png')
    clear = load_font('resource/ENCR10B.TTF', 30)

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
                    game_framework.change_state(state.title_state)
                case pico2d.SDLK_q:
                    game_framework.quit()
                case pico2d.SDLK_SPACE:
                    game_framework.change_state(state.play_state)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == 1:
                for y in range(len(top)):
                    if top[y] < event.y < bottom[y]:
                        for x in range(len(left)):
                            if left[x] < event.x < right[x]:
                                server.stage = x + 1 + len(left) * y
                                game_framework.change_state(state.play_state)


def draw():
    global image, clear
    clear_canvas()
    image.draw(500, 300, 1000, 600)
    for y in range(len(top)):
        for x in range(len(left)):
            clear.draw(left[x] + 5, top[y], 'Clear', (255, 255, 255))
    
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
