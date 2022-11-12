import pico2d


right = 1
left = -1


class Monster1:
    def __init__(self):
        self.image = pico2d.load_image('resource/Monster1.png')
        self.x, self.y = 0, 0
        self.frame = [0, 1, 2, 3, 4, 3, 2, 1]
        self.what_frame = 0
        self.count = 0
        self.dir = right

    def update(self):
        self.count += 1
        if self.x > 1000:
            self.dir = left
        elif self.x < 0:
            self.dir = right

        if self.dir == right:
            self.x += 0.5
        else:
            self.x -= 0.5

        if self.count % 50 == 0:
            self.what_frame = (self.what_frame + 1) % 7


    def draw(self):
        if self.dir == right:
            self.image.clip_draw(self.frame[self.what_frame] * 42, 42, 42, 42, self.x, self.y)
        elif self.dir == left:
            self.image.clip_composite_draw(self.frame[self.what_frame] * 42, 42, 42, 42, 0, 'h', self.x, self.y, 42, 42)

