import pico2d


class Background:
    image = None
    exist = True

    def __init__(self):
        if Background.image is None:
            Background.image = pico2d.load_image('resource/Background.png')

    def draw(self):
        self.image.draw(500, 300, 1000, 600)

    def update(self):
        pass
