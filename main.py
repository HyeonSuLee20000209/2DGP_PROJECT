import pico2d
import game_framework

import state.select_state
import state.play_state

pico2d.open_canvas(1000, 600)
game_framework.run(state.select_state)
pico2d.close_canvas()
