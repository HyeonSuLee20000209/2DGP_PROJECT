import pico2d
import title_state
import play_state
import game_framework

pico2d.open_canvas(1000, 600)

background = pico2d.load_image('background.png')
background.draw_now(500, 300, 1000, 600)

play_state

pico2d.close_canvas()
