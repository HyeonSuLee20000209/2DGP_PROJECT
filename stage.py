import pico2d
from pico2d import *

from object.ground import Ground
from object.e_trap import ETrap
from object.spike import Spike
from object.double_jump import DoubleJump
from object.far_jump import FarJump
from object.star import Star
from object.jump_block import JumpBlock
from object.broken_block import BrokenBlock

import game_world
import server


s = [False for x in range(21)]


def stage(num):
    if num == 0:
        # for i in range(6):
        #     server.ground.append(Ground(25 + 50 * i, 25 + 50 * 0))
        # game_world.add_all_objects(server.ground, 2)
        # game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        for i in range(6):
            server.broken_block.append(BrokenBlock(25 + 50 * i, 25 + 50 * 0))
        game_world.add_all_objects(server.broken_block, 2)
        game_world.add_collision_pairs(server.p, server.broken_block, 'p:bb')

        server.star.append(Star(25 + 50 * 7, 25 + 50 * 2))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 1:
        pass
    elif num == 2:
        pass
    elif num == 3:
        pass
    elif num == 4:
        pass
    elif num == 5:
        pass
    elif num == 6:
        pass
    elif num == 7:
        for i in range(5):
            server.ground.append(Ground(25 + 50 * i, 25 + 50 * 0))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        server.fj.append(FarJump(25 + 50 * 7, 25 + 50 * 2))
        game_world.add_all_objects(server.fj, 3)
        game_world.add_collision_pairs(server.p, server.fj, 'p:fj')
    elif num == 8:
        pass
    elif num == 9:
        pass
    elif num == 10:
        pass
    elif num == 11:
        pass
    elif num == 12:
        pass
    elif num == 13:
        pass
    elif num == 14:
        for i in range(6):
            server.ground.append(Ground(25 + 50 * i, 25 + 50 * 0))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        server.fj.append(FarJump(25 + 50 * 7, 25 + 50 * 2))
        game_world.add_all_objects(server.fj, 3)
        game_world.add_collision_pairs(server.p, server.fj, 'p:fj')
    elif num == 15:
        pass
    elif num == 16:
        pass
    elif num == 17:
        pass
    elif num == 18:
        pass
    elif num == 19:
        pass
    elif num == 20:
        pass


def stage2():
    # server.fj.append(FarJump(25 + 50 * 7, 25 + 50 * 2))
    # game_world.add_all_objects(server.fj, 3)
    # game_world.add_collision_pairs(server.p, server.fj, 'p:fj')
    #
    # global e_trap
    # game_world.add_all_objects(e_trap, 2)
    # game_world.add_collision_pairs(p, e_trap, 'p:e_trap')
    #
    # global spike
    # game_world.add_all_objects(spike, 2)
    # game_world.add_collision_pairs(p, spike, 'p:spike')
    #
    # global dj
    # game_world.add_all_objects(dj, 3)
    # game_world.add_collision_pairs(p, dj, 'p:dj')
    #
    # global fj
    # game_world.add_all_objects(fj, 3)
    # game_world.add_collision_pairs(p, fj, 'p:fj')
    #
    # global star
    # game_world.add_all_objects(star, 4)
    # game_world.add_collision_pairs(p, star, 'p:star')

    pass

