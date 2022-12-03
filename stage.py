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
from object.broken_jump_block import BrokenJumpBlock

import game_world
import server


s = [False for x in range(21)]


def stage(num):
    if num == 0:
        server.ground.append(Ground(25 + 50 * 2, 25 + 50 * 4))
        server.ground.append(Ground(25 + 50 * 3, 25 + 50 * 3))
        server.ground.append(Ground(25 + 50 * 16, 25 + 50 * 3))
        server.ground.append(Ground(25 + 50 * 17, 25 + 50 * 4))
        for i in range(4):
            server.ground.append(Ground(25 + 50 * 1, 25 + 50 * (5 + i)))
            server.ground.append(Ground(25 + 50 * 18, 25 + 50 * (5 + i)))
        for i in range(12):
            server.ground.append(Ground(25 + 50 * (4 + i), 25 + 50 * 2))
            server.star.append(Star(25 + 50 * (4 + i), 25 + 50 * 3))
            server.star.append(Star(25 + 50 * (4 + i), 25 + 50 * 4))

        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')

    elif num == 1:
        for i in range(5):
            server.ground.append(Ground(25 + 50 * i, 25 + 50 * 0))
        server.ground.append(Ground(25 + 50 * 2, 25 + 50 * 1))
        server.ground.append(Ground(25 + 50 * 15, 25 + 50 * 0))
        server.ground.append(Ground(25 + 50 * 19, 25 + 50 * 1))
        server.ground.append(Ground(25 + 50 * 12, 25 + 50 * 7))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        server.spike.append(Spike(25 + 50 * 3, 25 + 50 * 1))
        game_world.add_all_objects(server.spike, 2)
        game_world.add_collision_pairs(server.p, server.spike, 'p:spike')

        server.jump_block.append(JumpBlock(25 + 50 * 7, 25 + 50 * 0))
        game_world.add_all_objects(server.jump_block, 3)
        game_world.add_collision_pairs(server.p, server.jump_block, 'p:jb')

        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 10, 25 + 50 * 0))
        game_world.add_all_objects(server.broken_jump_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_jump_block, 'p:bjb')

        server.fj.append(FarJump(25 + 50 * 12, 25 + 50 * 9))
        game_world.add_all_objects(server.fj, 3)
        game_world.add_collision_pairs(server.p, server.fj, 'p:fj')

        for i in range(3):
            server.e_trap.append(ETrap(25 + 50 * 8, 25 + 50 * i))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        server.broken_block.append(BrokenBlock(25 + 50 * 18, 25 + 50 * 0))
        for i in range(4):
            server.broken_block.append(BrokenBlock(25 + 50 * (16 - i), 25 + 50 * (3 + i)))
        game_world.add_all_objects(server.broken_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_block, 'p:bb')

        server.dj.append(DoubleJump(25 + 50 * 19, 25 + 50 * 2))
        game_world.add_all_objects(server.dj, 3)
        game_world.add_collision_pairs(server.p, server.dj, 'p:dj')

        server.star.append(Star(25 + 50 * 3, 25 + 50 * 5))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 2:
        server.star.append(Star(25 + 50 * 5, 25 + 50 * 3))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 3:
        pass
    elif num == 4:
        pass
    elif num == 5:
        pass
    elif num == 6:
        pass
    elif num == 7:
        for i in range(10):
            server.ground.append(Ground(25 + 50 * (i + 1), 25 + 50 * 0))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')
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
        server.ground.append(Ground(25 + 50 * 2, 25 + 50 * 9))
        server.ground.append(Ground(25 + 50 * 1, 25 + 50 * 6))
        server.ground.append(Ground(25 + 50 * 3, 25 + 50 * 3))
        server.ground.append(Ground(25 + 50 * 1, 25 + 50 * 0))
        server.ground.append(Ground(25 + 50 * 10, 25 + 50 * 9))
        server.ground.append(Ground(25 + 50 * 17, 25 + 50 * 9))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        for i in range(3):
            server.e_trap.append(ETrap(25 + 50 * 2, 25 + 50 * i * 3))
            server.e_trap.append(ETrap(25 + 50 * 10, 25 + 50 * i * 3))
            server.e_trap.append(ETrap(25 + 50 * 17, 25 + 50 * i * 3))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        server.dj.append(DoubleJump(25 + 50 * 18, 25 + 50 * 1))
        server.dj.append(DoubleJump(25 + 50 * 16, 25 + 50 * 4))
        server.dj.append(DoubleJump(25 + 50 * 18, 25 + 50 * 7))
        game_world.add_all_objects(server.dj, 3)
        game_world.add_collision_pairs(server.p, server.dj, 'p:dj')

        server.broken_block.append(BrokenBlock(25 + 50 * 9, 25 + 50 * 6))
        server.broken_block.append(BrokenBlock(25 + 50 * 11, 25 + 50 * 3))
        server.broken_block.append(BrokenBlock(25 + 50 * 9, 25 + 50 * 0))
        game_world.add_all_objects(server.broken_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_block, 'p:bb')

        for i in range(3):
            server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * (4 + i), 25 + 50 * i * 3))
            server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * (12 + i), 25 + 50 * i * 3))
        game_world.add_all_objects(server.broken_jump_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_jump_block, 'p:bjb')

        for i in range(3):
            server.star.append(Star(25 + 50 * 2, 25 + 50 * (1 + 3 * i)))
            server.star.append(Star(25 + 50 * 10, 25 + 50 * (1 + 3 * i)))
            server.star.append(Star(25 + 50 * 17, 25 + 50 * (1 + 3 * i)))
        server.star.append(Star(25 + 50 * 10, 25 + 50 * 10))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
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

    server.star_count = len(server.star)


def stage2():
    server.fj.append(FarJump(25 + 50 * 7, 25 + 50 * 2))
    game_world.add_all_objects(server.fj, 3)
    game_world.add_collision_pairs(server.p, server.fj, 'p:fj')

    server.e_trap.append(ETrap())
    game_world.add_all_objects(server.e_trap, 2)
    game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

    server.spike.append(Spike())
    game_world.add_all_objects(server.spike, 2)
    game_world.add_collision_pairs(server.p, server.spike, 'p:spike')

    server.dj.append(DoubleJump(25 + 50 * 10, 25 + 50 * 6))
    game_world.add_all_objects(server.dj, 3)
    game_world.add_collision_pairs(server.p, server.dj, 'p:dj')

    server.fj.append(FarJump())
    game_world.add_all_objects(server.fj, 3)
    game_world.add_collision_pairs(server.p, server.fj, 'p:fj')

    server.broken_block.append(BrokenBlock)
    game_world.add_all_objects(server.broken_block, 3)
    game_world.add_collision_pairs(server.p, server.broken_block, 'p:bb')

    server.broken_jump_block.append(BrokenJumpBlock)
    game_world.add_all_objects(server.broken_jump_block, 3)
    game_world.add_collision_pairs(server.p, server.broken_jump_block, 'p:bjb')

    server.jump_block.append(JumpBlock)
    game_world.add_all_objects(server.jump_block, 3)
    game_world.add_collision_pairs(server.p, server.broken_jump_block, 'p:jb')

    server.star.append(Star(25 + 50 * 7, 25 + 50 * 2))
    game_world.add_all_objects(server.star, 4)
    game_world.add_collision_pairs(server.p, server.star, 'p:star')
