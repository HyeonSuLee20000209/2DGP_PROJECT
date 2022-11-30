import pico2d
from pico2d import *

from object.ground import Ground
from object.e_trap import ETrap
from object.spike import Spike
from object.double_jump import DoubleJump
from object.far_jump import FarJump
from object.star import Star
from object.jump_block import JumpBlock

import game_world
import server


def stage(num):
    if num == 1:
        for i in range(6):
            server.ground.append(Ground(25 + 50 * i, 25 + 50 * 0))
            # server.ground.append(Ground(25 + 50 * (i + 1), 25 + 50 * 2))
            # server.ground.append(Ground(25 + 50 * 5, 25 + 50 * i))
            # server.ground.append(Ground(25 + 50 * 1, 25 + 50 * i))
            # server.ground.append(Ground(25 + 50 * (i + i + i + 1), 25 + 50 * 1))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        server.fj.append(FarJump(25 + 50 * 7, 25 + 50 * 2))
        game_world.add_all_objects(server.fj, 3)
        game_world.add_collision_pairs(server.p, server.fj, 'p:fj')
    elif num == 8:
        for i in range(8):
            server.ground.append(Ground(25 + 50 * i, 25 + 50 * 0))
            game_world.add_all_objects(server.ground, 2)
            game_world.add_collision_pairs(server.p, server.ground, 'p:ground')
    elif num == 15:
        for i in range(5):
            server.ground.append(Ground(25 + 50 * i, 25 + 50 * 0))
            game_world.add_all_objects(server.ground, 2)
            game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        server.dj.append(DoubleJump(25 + 50 * 7, 25 + 50 * 2))
        game_world.add_all_objects(server.dj, 3)
        game_world.add_collision_pairs(server.p, server.dj, 'p:dj')


def stage2():
    # global e_trap
    # game_world.add_all_objects(e_trap, 2)
    #
    # game_world.add_collision_pairs(p, e_trap, 'p:e_trap')
    #
    # global spike
    # game_world.add_all_objects(spike, 2)
    #
    # game_world.add_collision_pairs(p, spike, 'p:spike')
    #
    # global dj
    # game_world.add_all_objects(dj, 3)
    #
    # game_world.add_collision_pairs(p, dj, 'p:dj')
    #
    # global fj
    # game_world.add_all_objects(fj, 3)
    #
    # game_world.add_collision_pairs(p, fj, 'p:fj')
    #
    # global star
    # game_world.add_all_objects(star, 4)
    #
    # game_world.add_collision_pairs(p, star, 'p:star')

    pass

