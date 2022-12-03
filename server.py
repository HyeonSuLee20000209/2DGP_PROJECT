p = None
bg = None

stage = 0

ground = []
broken_block = []
broken_jump_block = []
e_trap = []
spike = []
dj = []
fj = []
jump_block = []
star = []
star_count = 0
monster1 = []
monster2 = []


def clear():
    global p
    p = None

    global bg
    bg = None

    global ground, broken_block, e_trap, spike, monster1, monster2
    ground, broken_block, e_trap, spike, monster1, monster2 = [], [], [], [], [], []

    global dj, fj, jump_block, broken_jump_block
    dj, fj, jump_block, broken_jump_block = [], [], [], []

    global star
    star = []

    global stage
    stage = 0

    global star_count
    star_count = 0
