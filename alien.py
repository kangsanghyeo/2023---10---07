from pygame.color import Color
from animation import Animation

class Alien(Animation):
    def __init__(self):
        self.sprite_image = 'alien.png'
        self.sprite_width = 32
        self.sprite_height = 32
        self.sprite_columns = 3
        self.fps = 10
        self.init_animation()

    def forward(self):
        if self.rect.x < 500:
            self.rect.x += 1

    def backward(self):
        if self.rect.x > 200:
            self.rect.x -= 1

    def update(self):
        self.calc_next_frame()

        rect = (self.sprite_width*self.current_frame, 0,
                self.sprite_width, self.sprite_height)
        self.image.blit( self.sprite_sheet, (0, 0), rect)
        self.image.set_colorkey(Color(255, 0, 255))
        
