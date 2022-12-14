# 0 배경, 1 플레이어, 2 땅, 3 아이템, 4 별
objects = [[], [], [], [], []]
collision_group = dict()


def add_object(o, depth):
    objects[depth].append(o)


def add_all_objects(ol, depth):
    objects[depth] += ol


def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')


def all_objects():
    for layer in objects:
        for o in layer:
            yield o


def clear():
    for o in all_objects():
        remove_collision_object(o)
        del o
    for layer in objects:
        layer.clear()


def layer_objects(num):
    for o in objects[num]:
        yield o


def layer_clear(num):
    for o in layer_objects(num):
        del o


def add_collision_pairs(a, b, group):
    if group not in collision_group:
        collision_group[group] = [[], []]

    if a:
        if type(a) is list:
            # 객체 리스트 추가
            collision_group[group][0] += a
        else:
            # 단일 객체 추가
            collision_group[group][0].append(a)

    if b:
        if type(b) is list:
            # 객체 리스트 추가
            collision_group[group][1] += b
        else:
            # 단일 객체 추가
            collision_group[group][1].append(b)


def all_collision_pairs():
    # key, value 다 가져옴
    for group, pairs in collision_group.items():
        for a in pairs[0]:
            for b in pairs[1]:
                yield a, b, group


def remove_collision_object(o):
    for pairs in collision_group.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        elif o in pairs[1]:
            pairs[1].remove(o)
