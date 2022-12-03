import pico2d


class Background:
    image = None
    exist = True
    bgm = None

    def __init__(self):
        if Background.image is None:
            Background.image = pico2d.load_image('resource/Background.png')
        if Background.bgm is None:
            Background.bgm = pico2d.load_music('resource/GreenGreens.mp3')
            self.bgm.set_volume(32)
            self.bgm.repeat_play()

    def draw(self):
        self.image.draw(500, 300, 1000, 600)

    def update(self):
        pass
