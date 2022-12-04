from object.ground import Ground
from object.e_trap import ETrap
from object.spike import Spike
from object.double_jump import DoubleJump
from object.far_jump import FarJump
from object.star import Star
from object.jump_block import JumpBlock
from object.broken_block import BrokenBlock
from object.broken_jump_block import BrokenJumpBlock
from object.monster1 import Monster1
from object.monster2 import Monster2
from object.shootblock import ShootBlockRight, ShootBlockLeft

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
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        server.monster1.append(Monster1(25 + 50 * 4, 25 + 50 * 3))
        game_world.add_all_objects(server.monster1, 2)
        game_world.add_collision_pairs(server.p, server.monster1, 'p:m1')
        game_world.add_collision_pairs(server.ground, server.monster1, 'g:m1')

        for i in range(12):
            server.star.append(Star(25 + 50 * (4 + i), 25 + 50 * 4))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 1:
        server.e_trap.append(ETrap(25 + 50 * 0, 25 + 50 * 4))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        for i in range(15):
            server.ground.append(Ground(25 + 50 * (1 + i), 25 + 50 * 4))

            server.ground.append(Ground(25 + 50 * (3 + i), 25 + 50 * 0))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        for i in range(4):
            server.spike.append(Spike(25 + 50 * (3 + 2 * i), 25 + 50 * 5))
        for i in range(2):
            server.spike.append(Spike(25 + 50 * (10 + i), 25 + 50 * 5))
            server.spike.append(Spike(25 + 50 * (11 + i), 25 + 50 * 1))
            server.spike.append(Spike(25 + 50 * (6 + i), 25 + 50 * 1))
        server.spike.append(Spike(25 + 50 * 17, 25 + 50 * 1))
        game_world.add_all_objects(server.spike, 2)
        game_world.add_collision_pairs(server.p, server.spike, 'p:spike')

        server.dj.append(DoubleJump(25 + 50 * 9, 25 + 50 * 6))
        game_world.add_all_objects(server.dj, 3)
        game_world.add_collision_pairs(server.p, server.dj, 'p:dj')

        server.fj.append(FarJump(25 + 50 * 15, 25 + 50 * 2))
        server.fj.append(FarJump(25 + 50 * 10, 25 + 50 * 2))
        game_world.add_all_objects(server.fj, 3)
        game_world.add_collision_pairs(server.p, server.fj, 'p:fj')

        server.star.append(Star(25 + 50 * 17, 25 + 50 * 2))
        server.star.append(Star(25 + 50 * 17, 25 + 50 * 3))
        server.star.append(Star(25 + 50 * 1, 25 + 50 * 2))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 2:
        server.e_trap.append(ETrap(25 + 50 * 0, 25 + 50 * 4))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        for i in range(3):
            server.ground.append(Ground(25 + 50 * (1 + i), 25 + 50 * 4))
        for i in range(4):
            server.ground.append(Ground(25 + 50 * (5 + i), 25 + 50 * 4))
        server.ground.append(Ground(25 + 50 * 4, 25 + 50 * 3))
        for i in range(2):
            server.ground.append(Ground(25 + 50 * (9 + i), 25 + 50 * 3))
        for i in range(8):
            server.ground.append(Ground(25 + 50 * (11 + i), 25 + 50 * 4))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        for i in range(3):
            server.monster2.append(Monster2(25 + 50 * (13 + i), 25 + 50 * 5))
        for i in range(2):
            server.monster2.append(Monster2(25 + 50 * (9 + i), 25 + 50 * 4))
        server.monster2.append(Monster2(25 + 50 * 4, 25 + 50 * 4))
        server.monster2.append(Monster2(25 + 50 * 7, 25 + 50 * 5))
        server.monster2.append(Monster2(25 + 50 * 17, 25 + 50 * 5))
        game_world.add_all_objects(server.monster2, 2)
        game_world.add_collision_pairs(server.p, server.monster2, 'p:m2')
        game_world.add_collision_pairs(server.ground, server.monster2, 'g:m2')

        for i in range(2):
            server.star.append(Star(25 + 50 * 18, 25 + 50 * (5 + i)))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 3:
        server.ground.append(Ground(25 + 50 * 0, 25 + 50 * 0))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        for i in range(4):
            server.broken_block.append(BrokenBlock(25 + 50 * (3 + 2 * i), 25 + 50 * 0))
        game_world.add_all_objects(server.broken_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_block, 'p:bb')

        server.jump_block.append(JumpBlock(25 + 50 * 11, 25 + 50 * 0))
        server.jump_block.append(JumpBlock(25 + 50 * 18, 25 + 50 * 0))
        game_world.add_all_objects(server.jump_block, 3)
        game_world.add_collision_pairs(server.p, server.jump_block, 'p:jb')

        server.dj.append(DoubleJump(25 + 50 * 18, 25 + 50 * 3))
        game_world.add_all_objects(server.dj, 3)
        game_world.add_collision_pairs(server.p, server.dj, 'p:dj')

        for i in range(3):
            server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * (2 + 5 * i), 25 + 50 * 5))
        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 17, 25 + 50 * 4))
        game_world.add_all_objects(server.broken_jump_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_jump_block, 'p:bjb')

        for i in range(12):
            server.e_trap.append(ETrap(25 + 50 * 19, 25 + 50 * i))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        server.fj.append(FarJump(25 + 50 * 11, 25 + 50 * 4))
        game_world.add_all_objects(server.fj, 3)
        game_world.add_collision_pairs(server.p, server.fj, 'p:fj')

        for i in range(3):
            server.star.append(Star(25 + 50 * (0 + 5 * i), 25 + 50 * 9))
            server.star.append(Star(25 + 50 * 0, 25 + 50 * (6 + i)))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 4:
        server.ground.append(Ground(25 + 50 * 0, 25 + 50 * 9))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        for i in range(3):
            server.shoot_block_right.append(ShootBlockRight(25 + 50 * 1, 25 + 50 * (1 + 4 * i)))
        game_world.add_all_objects(server.shoot_block_right, 3)
        game_world.add_collision_pairs(server.p, server.shoot_block_right, 'p:sbr')

        for i in range(2):
            server.shoot_block_left.append(ShootBlockLeft(25 + 50 * 18, 25 + 50 * (3 + 4 * i)))
        game_world.add_all_objects(server.shoot_block_left, 3)
        game_world.add_collision_pairs(server.p, server.shoot_block_left, 'p:sbl')

        for i in range(6):
            server.star.append(Star(25 + 50 * (3 + 3 * i), 25 + 50 * 9))
            server.star.append(Star(25 + 50 * (1 + 3 * i), 25 + 50 * 7))
            server.star.append(Star(25 + 50 * (3 + 3 * i), 25 + 50 * 5))
            server.star.append(Star(25 + 50 * (1 + 3 * i), 25 + 50 * 3))
            server.star.append(Star(25 + 50 * (3 + 3 * i), 25 + 50 * 1))

        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')

        for i in range(9):
            server.e_trap.append(ETrap(25 + 50 * 0, 25 + 50 * i))
        for i in range(12):
            server.e_trap.append(ETrap(25 + 50 * 19, 25 + 50 * i))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')
    elif num == 5:
        for i in range(4):
            server.ground.append(Ground(25 + 50 * 3 * i, 25 + 50 * 3))
        for i in range(3):
            server.ground.append(Ground(25 + 50 * 4, 25 + 50 * (5 + i)))
        for i in range(5):
            server.ground.append(Ground(25 + 50 * 11, 25 + 50 * (5 + i)))
        server.ground.append(Ground(25 + 50 * 17, 25 + 50 * 4))
        server.ground.append(Ground(25 + 50 * 18, 25 + 50 * 4))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        for i in range(2):
            server.spike.append(Spike(25 + 50 * (4 + i), 25 + 50 * 3))
            server.spike.append(Spike(25 + 50 * (7 + i), 25 + 50 * 3))
        server.spike.append(Spike(25 + 50 * 11, 25 + 50 * 10))
        game_world.add_all_objects(server.spike, 2)
        game_world.add_collision_pairs(server.p, server.spike, 'p:spike')

        server.shoot_block_right.append(ShootBlockRight(25 + 50 * 13, 25 + 50 * 5))
        game_world.add_all_objects(server.shoot_block_right, 3)
        game_world.add_collision_pairs(server.p, server.shoot_block_right, 'p:sbr')

        server.shoot_block_left.append(ShootBlockLeft(25 + 50 * 10, 25 + 50 * 4))
        server.shoot_block_left.append(ShootBlockLeft(25 + 50 * 15, 25 + 50 * 3))
        server.shoot_block_left.append(ShootBlockLeft(25 + 50 * 11, 25 + 50 * 1))
        game_world.add_all_objects(server.shoot_block_left, 3)
        game_world.add_collision_pairs(server.p, server.shoot_block_left, 'p:sbl')

        server.jump_block.append(JumpBlock(25 + 50 * 1, 25 + 50 * 4))
        server.jump_block.append(JumpBlock(25 + 50 * 3, 25 + 50 * 7))
        game_world.add_all_objects(server.jump_block, 3)
        game_world.add_collision_pairs(server.p, server.jump_block, 'p:jb')

        for i in range(3):
            server.e_trap.append(ETrap(25 + 50 * 3, 25 + 50 * i))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        for i in range(3):
            server.broken_block.append(BrokenBlock(25 + 50 * (5 + 2 * i), 25 + 50 * 10))
        game_world.add_all_objects(server.broken_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_block, 'p:bb')

        server.star.append(Star(25 + 50 * 4, 25 + 50 * 1))
        server.star.append(Star(25 + 50 * 4, 25 + 50 * 0))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 6:
        for i in range(3):
            server.ground.append(Ground(25 + 50 * (3 + 5 * i), 25 + 50 * 9))
            server.ground.append(Ground(25 + 50 * (4 + 3 * i), 25 + 50 * 5))
        for i in range(4):
            server.ground.append(Ground(25 + 50 * (3 + 3 * i), 25 + 50 * 0))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        for i in range(9):
            for j in range(2):
                server.e_trap.append(ETrap(25 + 50 * (5 + 6 * j), 25 + 50 * (3 + i)))
                server.e_trap.append(ETrap(25 + 50 * (8 + 6 * j), 25 + 50 * (0 + i)))
            server.e_trap.append(ETrap(25 + 50 * 17, 25 + 50 * (0 + i)))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 7, 25 + 50 * 0))
        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 6, 25 + 50 * 3))
        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 6, 25 + 50 * 7))
        game_world.add_all_objects(server.broken_jump_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_jump_block, 'p:bjb')

        server.broken_block.append(BrokenBlock(25 + 50 * 12, 25 + 50 * 3))
        server.broken_block.append(BrokenBlock(25 + 50 * 12, 25 + 50 * 7))
        server.broken_block.append(BrokenBlock(25 + 50 * 13, 25 + 50 * 1))
        server.broken_block.append(BrokenBlock(25 + 50 * 13, 25 + 50 * 5))
        game_world.add_all_objects(server.broken_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_block, 'p:bb')

        server.dj.append(DoubleJump(25 + 50 * 7, 25 + 50 * 6))
        server.dj.append(DoubleJump(25 + 50 * 13, 25 + 50 * 2))
        server.dj.append(DoubleJump(25 + 50 * 13, 25 + 50 * 6))
        server.dj.append(DoubleJump(25 + 50 * 12, 25 + 50 * 4))
        server.dj.append(DoubleJump(25 + 50 * 12, 25 + 50 * 8))
        game_world.add_all_objects(server.dj, 3)
        game_world.add_collision_pairs(server.p, server.dj, 'p:dj')

        server.spike.append(Spike(25 + 50 * 10, 25 + 50 * 6))
        game_world.add_all_objects(server.spike, 2)
        game_world.add_collision_pairs(server.p, server.spike, 'p:spike')

        server.shoot_block_right.append(ShootBlockRight(25 + 50 * 14, 25 + 50 * 9))
        game_world.add_all_objects(server.shoot_block_right, 3)
        game_world.add_collision_pairs(server.p, server.shoot_block_right, 'p:sbr')

        for i in range(9):
            server.star.append(Star(25 + 50 * 18, 25 + 50 * i))
            server.star.append(Star(25 + 50 * 19, 25 + 50 * i))
        server.star.append(Star(25 + 50 * 4, 25 + 50 * 6))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 7:
        for i in range(12):
            for j in range(3):
                server.ground.append(Ground(25 + 50 * (4 + i), 25 + 50 * (0 + j * 4)))
        for i in range(3):
            server.ground.append(Ground(25 + 50 * 3, 25 + 50 * (1 + i * 4)))
            server.ground.append(Ground(25 + 50 * 16, 25 + 50 * (1 + i * 4)))
            server.ground.append(Ground(25 + 50 * i, 25 + 50 * 9))
            server.ground.append(Ground(25 + 50 * (17 + i), 25 + 50 * 5))
            server.ground.append(Ground(25 + 50 * i, 25 + 50 * 1))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        server.monster1.append(Monster1(25 + 50 * 4, 25 + 50 * 1))
        server.monster1.append(Monster1(25 + 50 * 4, 25 + 50 * 5))
        server.monster1.append(Monster1(25 + 50 * 15, 25 + 50 * 5))
        server.monster1.append(Monster1(25 + 50 * 4, 25 + 50 * 9))
        game_world.add_all_objects(server.monster1, 2)
        game_world.add_collision_pairs(server.p, server.monster1, 'p:m1')
        game_world.add_collision_pairs(server.ground, server.monster1, 'g:m1')

        for i in range(12):
            for j in range(3):
                server.star.append(Star(25 + 50 * (4 + i), 25 + 50 * (2 + 4 * j)))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 8:
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
        game_world.add_all_objects(server.jump_block, 2)
        game_world.add_collision_pairs(server.p, server.jump_block, 'p:jb')

        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 10, 25 + 50 * 0))
        game_world.add_all_objects(server.broken_jump_block, 2)
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
    elif num == 9:
        server.ground.append(Ground(25 + 50 * 12, 25 + 50 * 8))
        server.ground.append(Ground(25 + 50 * 16, 25 + 50 * 8))
        for i in range(2):
            server.ground.append(Ground(25 + 50 * (18 + i), 25 + 50 * 8))
        for i in range(5):
            server.ground.append(Ground(25 + 50 * (2 + i), 25 + 50 * 7))
        server.ground.append(Ground(25 + 50 * 1, 25 + 50 * 8))
        server.ground.append(Ground(25 + 50 * 7, 25 + 50 * 8))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        server.monster1.append(Monster1(25 + 50 * 2, 25 + 50 * 8))
        game_world.add_all_objects(server.monster1, 2)
        game_world.add_collision_pairs(server.p, server.monster1, 'p:m1')
        game_world.add_collision_pairs(server.ground, server.monster1, 'g:m1')

        server.monster2.append(Monster2(25 + 50 * 12, 25 + 50 * 9))
        game_world.add_all_objects(server.monster2, 2)
        game_world.add_collision_pairs(server.p, server.monster2, 'p:m2')
        game_world.add_collision_pairs(server.ground, server.monster2, 'g:m2')

        server.jump_block.append(JumpBlock(25 + 50 * 9, 25 + 50 * 7))
        game_world.add_all_objects(server.jump_block, 2)
        game_world.add_collision_pairs(server.p, server.jump_block, 'p:jb')

        server.dj.append(DoubleJump(25 + 50 * 2, 25 + 50 * 2))
        server.dj.append(DoubleJump(25 + 50 * 15, 25 + 50 * 2))
        game_world.add_all_objects(server.dj, 3)
        game_world.add_collision_pairs(server.p, server.dj, 'p:dj')

        server.fj.append(FarJump(25 + 50 * 16, 25 + 50 * 9))
        game_world.add_all_objects(server.fj, 3)
        game_world.add_collision_pairs(server.p, server.fj, 'p:fj')

        for i in range(10):
            server.e_trap.append(ETrap(25 + 50 * (10 + i), 25 + 50 * 7))
        for i in range(3):
            server.e_trap.append(ETrap(25 + 50 * 8, 25 + 50 * (7 + i)))
        server.e_trap.append(ETrap(25 + 50 * 8, 25 + 50 * 7))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        for i in range(5):
            server.broken_block.append(BrokenBlock(25 + 50 * (5 + (2 * i + 1)), 25 + 50 * 0))
        game_world.add_all_objects(server.broken_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_block, 'p:bb')

        for i in range(3):
            server.star.append(Star(25 + 50 * (7 + i), 25 + 50 * 11))
        for i in range(5):
            server.star.append(Star(25 + 50 * (2 + i), 25 + 50 * 8))
        for i in range(8):
            server.star.append(Star(25 + 50 * (6 + i), 25 + 50 * 1))
        for i in range(2):
            server.star.append(Star(25 + 50 * (18 + i), 25 + 50 * 0))
            server.star.append(Star(25 + 50 * (18 + i), 25 + 50 * 1))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 10:
        for i in range(17):
            server.ground.append(Ground(25 + 50 * i, 25 + 50 * 7))
        server.ground.append(Ground(25 + 50 * 16, 25 + 50 * 4))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        server.dj.append(DoubleJump(25 + 50 * 2, 25 + 50 * 8))
        for i in range(4):
            server.dj.append(DoubleJump(25 + 50 * (5 + (2 * i + 1)), 25 + 50 * 9))
        for i in range(5):
            server.dj.append(DoubleJump(25 + 50 * (5 + (2 * i + 1)), 25 + 50 * 1))
        server.dj.append(DoubleJump(25 + 50 * 3, 25 + 50 * 1))
        server.dj.append(DoubleJump(25 + 50 * 17, 25 + 50 * 4))
        game_world.add_all_objects(server.dj, 3)
        game_world.add_collision_pairs(server.p, server.dj, 'p:dj')

        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 17, 25 + 50 * 0))
        game_world.add_all_objects(server.broken_jump_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_jump_block, 'p:bjb')

        for i in range(3):
            server.e_trap.append(ETrap(25 + 50 * (3 + i), 25 + 50 * 8))
        for i in range(4):
            server.e_trap.append(ETrap(25 + 50 * 16, 25 + 50 * i))
        for i in range(12):
            server.e_trap.append(ETrap(25 + 50 * (4 + i), 25 + 50 * 0))
        server.e_trap.append(ETrap(25 + 50 * 17, 25 + 50 * 7))
        server.e_trap.append(ETrap(25 + 50 * 18, 25 + 50 * 6))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        for i in range(10):
            server.spike.append(Spike(25 + 50 * (6 + i), 25 + 50 * 8))
        game_world.add_all_objects(server.spike, 2)
        game_world.add_collision_pairs(server.p, server.spike, 'p:spike')

        for i in range(10):
            server.star.append(Star(25 + 50 * (6 + i), 25 + 50 * 10))
            server.star.append(Star(25 + 50 * (6 + i), 25 + 50 * 2))
        server.star.append(Star(25 + 50 * 1, 25 + 50 * 0))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 11:
        for i in range(5):
            server.ground.append(Ground(25 + 50 * (14 + i), 25 + 50 * 8))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        server.fj.append(FarJump(25 + 50 * 14, 25 + 50 * 9))
        game_world.add_all_objects(server.fj, 3)
        game_world.add_collision_pairs(server.p, server.fj, 'p:fj')

        for i in range(7):
            server.star.append(Star(25 + 50 * (1 + i), 25 + 50 * i))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 12:
        for i in range(5):
            server.ground.append(Ground(25 + 50 * (15 + i), 25 + 50 * 8))
            server.ground.append(Ground(25 + 50 * (1 + i), 25 + 50 * 0))
            server.ground.append(Ground(25 + 50 * (1 + i), 25 + 50 * 8))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        server.fj.append(FarJump(25 + 50 * 15, 25 + 50 * 9))
        server.fj.append(FarJump(25 + 50 * 5, 25 + 50 * 9))
        game_world.add_all_objects(server.fj, 3)
        game_world.add_collision_pairs(server.p, server.fj, 'p:fj')

        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 0, 25 + 50 * 0))
        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 0, 25 + 50 * 6))
        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 1, 25 + 50 * 3))
        game_world.add_all_objects(server.broken_jump_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_jump_block, 'p:bjb')

        for i in range(5):
            server.e_trap.append(ETrap(25 + 50 * 19, 25 + 50 * (1 + i)))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        for i in range(7):
            server.star.append(Star(25 + 50 * (2 + i), 25 + 50 * (1 + i)))
        server.star.append(Star(25 + 50 * 19, 25 + 50 * 0))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
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
        game_world.add_all_objects(server.broken_block, 2)
        game_world.add_collision_pairs(server.p, server.broken_block, 'p:bb')

        for i in range(3):
            server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * (4 + i), 25 + 50 * i * 3))
            server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * (12 + i), 25 + 50 * i * 3))
        game_world.add_all_objects(server.broken_jump_block, 2)
        game_world.add_collision_pairs(server.p, server.broken_jump_block, 'p:bjb')

        for i in range(3):
            server.star.append(Star(25 + 50 * 2, 25 + 50 * (1 + 3 * i)))
            server.star.append(Star(25 + 50 * 10, 25 + 50 * (1 + 3 * i)))
            server.star.append(Star(25 + 50 * 17, 25 + 50 * (1 + 3 * i)))
        server.star.append(Star(25 + 50 * 10, 25 + 50 * 10))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 14:
        for i in range(3):
            server.ground.append(Ground(25 + 50 * i, 25 + 50 * 0))
        for i in range(3):
            server.ground.append(Ground(25 + 50 * 1, 25 + 50 * (3 + 3 * i)))
            server.ground.append(Ground(25 + 50 * (12 + i), 25 + 50 * 1))

        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        for i in range(6):
            server.e_trap.append(ETrap(25 + 50 * 0, 25 + 50 * (3 + i)))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        server.dj.append(DoubleJump(25 + 50 * 2, 25 + 50 * 1))
        server.dj.append(DoubleJump(25 + 50 * 10, 25 + 50 * 6))
        server.dj.append(DoubleJump(25 + 50 * 14, 25 + 50 * 7))
        game_world.add_all_objects(server.dj, 3)
        game_world.add_collision_pairs(server.p, server.dj, 'p:dj')

        for i in range(4):
            server.spike.append(Spike(25 + 50 * (11 + i), 25 + 50 * 5))
        for i in range(2):
            server.spike.append(Spike(25 + 50 * (5 + i), 25 + 50 * 2))
            server.spike.append(Spike(25 + 50 * (7 + i), 25 + 50 * 3))
            server.spike.append(Spike(25 + 50 * (9 + i), 25 + 50 * 4))
        game_world.add_all_objects(server.spike, 2)
        game_world.add_collision_pairs(server.p, server.spike, 'p:spike')

        server.e_trap.append(ETrap(25 + 50 * 12, 25 + 50 * 6))
        for i in range(2):
            server.e_trap.append(ETrap(25 + 50 * 15, 25 + 50 * (5 + i)))
        for i in range(5):
            server.e_trap.append(ETrap(25 + 50 * (15 + i), 25 + 50 * 1))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        for i in range(4):
            server.broken_block.append(BrokenBlock(25 + 50 * (4 + 2 * i), 25 + 50 * (2 + i)))
        server.broken_block.append(BrokenBlock(25 + 50 * 14, 25 + 50 * 6))
        game_world.add_all_objects(server.broken_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_block, 'p:bb')

        server.shoot_block_right.append(ShootBlockRight(25 + 50 * 11, 25 + 50 * 0))
        game_world.add_all_objects(server.shoot_block_right, 3)
        game_world.add_collision_pairs(server.p, server.shoot_block_right, 'p:sbr')

        server.star.append(Star(25 + 50 * 1, 25 + 50 * 4))
        server.star.append(Star(25 + 50 * 1, 25 + 50 * 7))
        for i in range(8):
            server.star.append(Star(25 + 50 * (12 + i), 25 + 50 * 0))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 15:
        server.ground.append(Ground(25 + 50 * 0, 25 + 50 * 7))
        server.ground.append(Ground(25 + 50 * 3, 25 + 50 * 0))
        server.ground.append(Ground(25 + 50 * 10, 25 + 50 * 0))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        for i in range(5):
            server.broken_block.append(BrokenBlock(25 + 50 * 1, 25 + 50 * (2 + i)))
            server.broken_block.append(BrokenBlock(25 + 50 * 2, 25 + 50 * (2 + i)))
        game_world.add_all_objects(server.broken_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_block, 'p:bb')

        server.e_trap.append(ETrap(25 + 50 * 1, 25 + 50 * 0))
        server.e_trap.append(ETrap(25 + 50 * 1, 25 + 50 * 1))
        server.e_trap.append(ETrap(25 + 50 * 2, 25 + 50 * 0))
        for i in range(7):
            server.e_trap.append(ETrap(25 + 50 * 0, 25 + 50 * i))
        for i in range(9):
            server.e_trap.append(ETrap(25 + 50 * 3, 25 + 50 * (3 + i)))
            server.e_trap.append(ETrap(25 + 50 * 7, 25 + 50 * (1 + i)))
            server.e_trap.append(ETrap(25 + 50 * 11, 25 + 50 * (3 + i)))
            server.e_trap.append(ETrap(25 + 50 * 16, 25 + 50 * (0 + i)))
            server.e_trap.append(ETrap(25 + 50 * 19, 25 + 50 * (0 + i)))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        server.jump_block.append(JumpBlock(25 + 50 * 6, 25 + 50 * 0))
        for i in range(3):
            server.jump_block.append(JumpBlock(25 + 50 * (13 + i), 25 + 50 * (3 * i)) )
        game_world.add_all_objects(server.jump_block, 3)
        game_world.add_collision_pairs(server.p, server.jump_block, 'p:jb')

        for i in range(3):
            server.dj.append(DoubleJump(25 + 50 * 4, 25 + 50 * (4 + 2 * i)))
            server.dj.append(DoubleJump(25 + 50 * 6, 25 + 50 * (5 + 2 * i)))
        game_world.add_all_objects(server.dj, 3)
        game_world.add_collision_pairs(server.p, server.dj, 'p:dj')

        for i in range(5):
            server.star.append(Star(25 + 50 * 1, 25 + 50 * (2 + i)))
            server.star.append(Star(25 + 50 * 2, 25 + 50 * (2 + i)))
        for i in range(9):
            server.star.append(Star(25 + 50 * 17, 25 + 50 * (0 + i)))
            server.star.append(Star(25 + 50 * 18, 25 + 50 * (0 + i)))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 16:
        for i in range(2):
            server.ground.append(Ground(25 + 50 * (1 + i), 25 + 50 * 5))
            server.ground.append(Ground(25 + 50 * (3 + i), 25 + 50 * 4))
            server.ground.append(Ground(25 + 50 * (5 + i), 25 + 50 * 3))
            server.ground.append(Ground(25 + 50 * (10 + i), 25 + 50 * 3))
            server.ground.append(Ground(25 + 50 * (12 + i), 25 + 50 * 4))
        for i in range(3):
            server.ground.append(Ground(25 + 50 * (7 + i), 25 + 50 * 2))
        server.ground.append(Ground(25 + 50 * 0, 25 + 50 * 6))
        server.ground.append(Ground(25 + 50 * 0, 25 + 50 * 7))
        server.ground.append(Ground(25 + 50 * 14, 25 + 50 * 5))
        server.ground.append(Ground(25 + 50 * 16, 25 + 50 * 6))
        server.ground.append(Ground(25 + 50 * 16, 25 + 50 * 7))
        server.ground.append(Ground(25 + 50 * 19, 25 + 50 * 7))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        server.monster2.append(Monster2(25 + 50 * 1, 25 + 50 * 6))
        server.monster2.append(Monster2(25 + 50 * 3, 25 + 50 * 5))
        server.monster2.append(Monster2(25 + 50 * 5, 25 + 50 * 4))
        server.monster2.append(Monster2(25 + 50 * 8, 25 + 50 * 3))
        server.monster2.append(Monster2(25 + 50 * 10, 25 + 50 * 4))
        server.monster2.append(Monster2(25 + 50 * 12, 25 + 50 * 5))
        server.monster2.append(Monster2(25 + 50 * 14, 25 + 50 * 6))
        game_world.add_all_objects(server.monster2, 2)
        game_world.add_collision_pairs(server.p, server.monster2, 'p:m2')
        game_world.add_collision_pairs(server.ground, server.monster2, 'g:m2')

        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 15, 25 + 50 * 5))
        game_world.add_all_objects(server.broken_jump_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_jump_block, 'p:bjb')

        for i in range(3):
            server.star.append(Star(25 + 50 * (7 + i), 25 + 50 * 3))
        for i in range(7):
            server.star.append(Star(25 + 50 * (5 + i), 25 + 50 * 4))
        for i in range(11):
            server.star.append(Star(25 + 50 * (3 + i), 25 + 50 * 5))
        for i in range(6):
            server.star.append(Star(25 + 50 * (1 + i), 25 + 50 * 6))
            server.star.append(Star(25 + 50 * (10 + i), 25 + 50 * 6))
        for i in range(4):
            server.star.append(Star(25 + 50 * (1 + i), 25 + 50 * 7))
            server.star.append(Star(25 + 50 * (12 + i), 25 + 50 * 7))
        server.star.append(Star(25 + 50 * 19, 25 + 50 * 8))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 17:
        for i in range(2):
            server.ground.append(Ground(25 + 50 * (12 + i), 25 + 50 * 9))
        for i in range(3):
            server.ground.append(Ground(25 + 50 * (9 + i), 25 + 50 * 5))
        for i in range(3):
            server.ground.append(Ground(25 + 50 * (3 + i), 25 + 50 * 0))
        for i in range(5):
            server.ground.append(Ground(25 + 50 * (3 + i), 25 + 50 * 5))
        server.ground.append(Ground(25 + 50 * 18, 25 + 50 * 0))
        server.ground.append(Ground(25 + 50 * 19, 25 + 50 * 1))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        for i in range(10):
            server.e_trap.append(ETrap(25 + 50 * (2 + i), 25 + 50 * 9))
            server.e_trap.append(ETrap(25 + 50 * 0, 25 + 50 * i))
        for i in range(9):
            server.e_trap.append(ETrap(25 + 50 * 2, 25 + 50 * i))
        for i in range(8):
            server.e_trap.append(ETrap(25 + 50 * 16, 25 + 50 * (2 + i)))
        server.e_trap.append(ETrap(25 + 50 * 17, 25 + 50 * 9))
        server.e_trap.append(ETrap(25 + 50 * 8, 25 + 50 * 5))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        server.fj.append(FarJump(25 + 50 * 12, 25 + 50 * 10))
        server.fj.append(FarJump(25 + 50 * 4, 25 + 50 * 6))
        game_world.add_all_objects(server.fj, 3)
        game_world.add_collision_pairs(server.p, server.fj, 'p:fj')

        server.shoot_block_right.append(ShootBlockRight(25 + 50 * 3, 25 + 50 * 1))
        game_world.add_all_objects(server.shoot_block_right, 3)
        game_world.add_collision_pairs(server.p, server.shoot_block_right, 'p:sbr')

        server.shoot_block_left.append(ShootBlockLeft(25 + 50 * 18, 25 + 50 * 10))
        game_world.add_all_objects(server.shoot_block_left, 3)
        game_world.add_collision_pairs(server.p, server.shoot_block_left, 'p:sbl')

        server.jump_block.append(JumpBlock(25 + 50 * 17, 25 + 50 * 2))
        server.jump_block.append(JumpBlock(25 + 50 * 19, 25 + 50 * 4))
        server.jump_block.append(JumpBlock(25 + 50 * 19, 25 + 50 * 7))
        game_world.add_all_objects(server.jump_block, 3)
        game_world.add_collision_pairs(server.p, server.jump_block, 'p:jb')

        for i in range(10):
            server.star.append(Star(25 + 50 * 1, 25 + 50 * i))
            game_world.add_all_objects(server.star, 4)
            game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 18:
        server.ground.append(Ground(25 + 50 * 1, 25 + 50 * 2))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        for i in range(4):
            server.spike.append(Spike(25 + 50 * (2 + i), 25 + 50 * 2))
        for i in range(4):
            server.spike.append(Spike(25 + 50 * (6 + i), 25 + 50 * 1))
        for i in range(3):
            server.spike.append(Spike(25 + 50 * (10 + i), 25 + 50 * 2))
            server.spike.append(Spike(25 + 50 * (13 + i), 25 + 50 * 3))
            server.spike.append(Spike(25 + 50 * (16 + i), 25 + 50 * 2))
        game_world.add_all_objects(server.spike, 2)
        game_world.add_collision_pairs(server.p, server.spike, 'p:spike')

        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 3, 25 + 50 * 3))
        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 7, 25 + 50 * 2))
        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 9, 25 + 50 * 2))
        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 13, 25 + 50 * 4))
        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 14, 25 + 50 * 4))
        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 17, 25 + 50 * 5))
        game_world.add_all_objects(server.broken_jump_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_jump_block, 'p:bjb')

        for i in range(5):
            server.broken_block.append(BrokenBlock(25 + 50 * (7 + i), 25 + 50 * 7))
        game_world.add_all_objects(server.broken_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_block, 'p:bb')

        for i in range(4):
            server.e_trap.append(ETrap(25 + 50 * i, 25 + 50 * 6))
            server.e_trap.append(ETrap(25 + 50 * i, 25 + 50 * 8))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        server.shoot_block_left.append(ShootBlockLeft(25 + 50 * 19, 25 + 50 * 7))
        game_world.add_all_objects(server.shoot_block_left, 3)
        game_world.add_collision_pairs(server.p, server.shoot_block_left, 'p:sbl')

        server.star.append(Star(25 + 50 * 0, 25 + 50 * 7))
        server.star.append(Star(25 + 50 * 7, 25 + 50 * 3))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 19:
        server.ground.append(Ground(25 + 50 * 0, 25 + 50 * 8))
        server.ground.append(Ground(25 + 50 * 3, 25 + 50 * 5))
        server.ground.append(Ground(25 + 50 * 14, 25 + 50 * 0))
        for i in range(8):
            server.ground.append(Ground(25 + 50 * 9, 25 + 50 * (2 + i)))
            server.ground.append(Ground(25 + 50 * 13, 25 + 50 * (2 + i)))
        for i in range(3):
            server.ground.append(Ground(25 + 50 * (10 + i), 25 + 50 * 0))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        server.shoot_block_right.append(ShootBlockRight(25 + 50 * 1, 25 + 50 * 8))
        server.shoot_block_right.append(ShootBlockRight(25 + 50 * 4, 25 + 50 * 5))
        server.shoot_block_right.append(ShootBlockRight(25 + 50 * 1, 25 + 50 * 1))
        game_world.add_all_objects(server.shoot_block_right, 3)
        game_world.add_collision_pairs(server.p, server.shoot_block_right, 'p:sbr')

        server.shoot_block_left.append(ShootBlockLeft(25 + 50 * 19, 25 + 50 * 1))
        server.shoot_block_left.append(ShootBlockLeft(25 + 50 * 19, 25 + 50 * 8))
        game_world.add_all_objects(server.shoot_block_left, 3)
        game_world.add_collision_pairs(server.p, server.shoot_block_left, 'p:sbl')

        for i in range(2):
            server.e_trap.append(ETrap(25 + 50 * 2, 25 + 50 * (8 + i)))
            server.e_trap.append(ETrap(25 + 50 * 5, 25 + 50 * (5 + i)))
            server.e_trap.append(ETrap(25 + 50 * 17, 25 + 50 * (2 + i)))
            server.e_trap.append(ETrap(25 + 50 * (14 + i), 25 + 50 * 9))
            server.e_trap.append(ETrap(25 + 50 * (14 + i), 25 + 50 * 7))

        for i in range(3):
            server.e_trap.append(ETrap(25 + 50 * i, 25 + 50 * 5))
            server.e_trap.append(ETrap(25 + 50 * 0, 25 + 50 * (1 + i)))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        server.dj.append(DoubleJump(25 + 50 * 1, 25 + 50 * 9))
        server.dj.append(DoubleJump(25 + 50 * 4, 25 + 50 * 6))
        server.dj.append(DoubleJump(25 + 50 * 17, 25 + 50 * 4))
        server.dj.append(DoubleJump(25 + 50 * 10, 25 + 50 * 4))
        server.dj.append(DoubleJump(25 + 50 * 10, 25 + 50 * 8))
        server.dj.append(DoubleJump(25 + 50 * 12, 25 + 50 * 6))
        game_world.add_all_objects(server.dj, 3)
        game_world.add_collision_pairs(server.p, server.dj, 'p:dj')

        server.fj.append(FarJump(25 + 50 * 8, 25 + 50 * 5))
        game_world.add_all_objects(server.fj, 3)
        game_world.add_collision_pairs(server.p, server.fj, 'p:fj')

        server.broken_block.append(BrokenBlock(25 + 50 * 8, 25 + 50 * 4))
        server.broken_block.append(BrokenBlock(25 + 50 * 10, 25 + 50 * 2))
        server.broken_block.append(BrokenBlock(25 + 50 * 10, 25 + 50 * 6))
        server.broken_block.append(BrokenBlock(25 + 50 * 12, 25 + 50 * 4))
        server.broken_block.append(BrokenBlock(25 + 50 * 12, 25 + 50 * 8))
        for i in range(3):
            server.broken_block.append(BrokenBlock(25 + 50 * (16 + i), 25 + 50 * 8))
        game_world.add_all_objects(server.broken_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_block, 'p:bb')

        server.broken_jump_block.append(BrokenJumpBlock(25 + 50 * 16, 25 + 50 * 1))
        game_world.add_all_objects(server.broken_jump_block, 3)
        game_world.add_collision_pairs(server.p, server.broken_jump_block, 'p:bjb')

        server.star.append(Star(25 + 50 * 14, 25 + 50 * 8))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    elif num == 20:
        server.ground.append(Ground(25 + 50 * 1, 25 + 50 * 9))
        game_world.add_all_objects(server.ground, 2)
        game_world.add_collision_pairs(server.p, server.ground, 'p:ground')

        for i in range(15):
            server.e_trap.append(ETrap(25 + 50 * (2 + i), 25 + 50 * 8))
            server.e_trap.append(ETrap(25 + 50 * (3 + i), 25 + 50 * 10))
        for i in range(11):
            server.e_trap.append(ETrap(25 + 50 * (8 + i), 25 + 50 * 6))
        for i in range(7):
            server.e_trap.append(ETrap(25 + 50 * (7 + i), 25 + 50 * 4))
        for i in range(4):
            server.e_trap.append(ETrap(25 + 50 * 18, 25 + 50 * (7 + i)))
            server.e_trap.append(ETrap(25 + 50 * 6, 25 + 50 * (4 + i)))
            server.e_trap.append(ETrap(25 + 50 * 15, 25 + 50 * (2 + i)))
            server.e_trap.append(ETrap(25 + 50 * (11 + i), 25 + 50 * 2))
            server.e_trap.append(ETrap(25 + 50 * (9 + i), 25 + 50 * 0))
        for i in range(3):
            server.e_trap.append(ETrap(25 + 50 * 9, 25 + 50 * (1 + i)))
        for i in range(2):
            server.e_trap.append(ETrap(25 + 50 * 14, 25 + 50 * (0 + i)))
        game_world.add_all_objects(server.e_trap, 2)
        game_world.add_collision_pairs(server.p, server.e_trap, 'p:e_trap')

        server.shoot_block_right.append(ShootBlockRight(25 + 50 * 2, 25 + 50 * 9))
        server.shoot_block_right.append(ShootBlockRight(25 + 50 * 7, 25 + 50 * 5))
        server.shoot_block_right.append(ShootBlockRight(25 + 50 * 10, 25 + 50 * 1))
        game_world.add_all_objects(server.shoot_block_right, 3)
        game_world.add_collision_pairs(server.p, server.shoot_block_right, 'p:sbr')

        server.shoot_block_left.append(ShootBlockLeft(25 + 50 * 17, 25 + 50 * 7))
        server.shoot_block_left.append(ShootBlockLeft(25 + 50 * 14, 25 + 50 * 3))
        game_world.add_all_objects(server.shoot_block_left, 3)
        game_world.add_collision_pairs(server.p, server.shoot_block_left, 'p:sbl')

        server.star.append(Star(25 + 50 * 13, 25 + 50 * 0))
        game_world.add_all_objects(server.star, 4)
        game_world.add_collision_pairs(server.p, server.star, 'p:star')
    server.star_count = len(server.star)
