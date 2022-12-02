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


def clear():
    global p
    p = None

    global bg
    bg = None

    global ground, broken_block, e_trap, spike
    ground, broken_block, e_trap, spike = [], [], [], []

    global dj, fj, jump_block, broken_jump_block
    dj, fj, jump_block, broken_jump_block = [], [], [], []

    global star
    star = []

    global stage
    stage = 0
