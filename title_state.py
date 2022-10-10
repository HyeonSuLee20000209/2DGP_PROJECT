from pico2d import *


image = True


def enter():
    global image
    image = load_image('title.png')


def end():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            # game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE or event.key == SDLK_q:
                # game_framework.quit()
            elif event.key == SDLK_SPACE:
                # game_framework.change_state(play_state)

def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass
