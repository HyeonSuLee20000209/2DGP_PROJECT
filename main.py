import pico2d
import title_state
import play_state
import game_framework

pico2d.open_canvas(1000, 700)
game_framework(play_state)
pico2d.close_canvas()
