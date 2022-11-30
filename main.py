import pico2d
import game_framework

import select_state
import play_state

pico2d.open_canvas(1000, 600)
game_framework.run(select_state)
pico2d.close_canvas()
