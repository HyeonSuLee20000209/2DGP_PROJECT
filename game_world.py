objects = [[], [], []]


def add_object(o, depth):
    objects[depth].append(o)


def add_all_objects(ol, depth):
    objects[depth] += ol


def remove_object(o):
    for layer in objects:
        if o in layer:
            # 리스트 삭제
            layer.remove(o)
            # 실제 메모리 삭제
            del o
            return
    raise ValueError('Trying destroy non existing object')


def all_objects():
    for layer in objects:
        for o in layer:
            yield o


def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()
