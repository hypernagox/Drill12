from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.m_bIsFire = False
        self.dead = False
    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
    def update(self):
        self.x += self.velocity * 100 * game_framework.frame_time

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

    # fill here
    def get_bb(self):
        return self.x - 10,self.y - 10,self.x + 10,self.y + 10
    def handle_collision(self,group,other):
        if group == 'boy:ball':
            if not self.m_bIsFire:
                game_world.remove_object(self)
        elif group == 'ball:zombie':
            if self.m_bIsFire:
                if self.dead:
                    return
                self.dead = True
                game_world.remove_object(self)
        else:
            pass