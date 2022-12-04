import pico2d


class ShootBlockRight:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.exist = True

        if ShootBlockRight.image is None:
            ShootBlockRight.image = pico2d.load_image('resource/ShootBlockRight.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def handle_collision(self, other, group):
        pass

    def handle_collision_dir(self, other, group, dir):
        pass


class ShootBlockLeft:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.exist = True

        if ShootBlockLeft.image is None:
            ShootBlockLeft.image = pico2d.load_image('resource/ShootBlockLeft.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def handle_collision(self, other, group):
        pass

    def handle_collision_dir(self, other, group, dir):
        pass
