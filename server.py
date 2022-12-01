p = None
bg = None

stage = 0

ground = []
broken_block = []
e_trap = []
spike = []
dj = []
fj = []
jblock = []
star = []


def clear():
    global p
    p = None

    global bg
    bg = None

    global ground, broken_block, e_trap, spike
    ground, broken_block, e_trap, spike = [], [], [], []

    global dj, fj, jblock
    dj, fj, jblock = [], [], []

    global star
    star = []

    global stage
    stage = 0
