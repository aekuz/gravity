from pygame import *

class wall(sprite.Sprite):

    def __init__(self,picture, x,y, width,height):
        self.picture = transform.scale(image.load(picture),(width,height))
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rect.top = self.rect.y
        self.rect.bottom = self.rect.y+height

    def place(self,win):
        win.blit(self.picture, (self.rect.x, self.rect.y))

class trap(sprite.Sprite):
    def __init__(self,picture, x,y, width,height):
        self.picture = transform.scale(image.load(picture),(width,height))
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y

    def place(self,win):
        win.blit(self.picture, (self.rect.x, self.rect.y))

