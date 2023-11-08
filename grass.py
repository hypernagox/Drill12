from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.dead = False
    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)


