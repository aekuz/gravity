from pygame import *

class main_hero_sprite(sprite.Sprite):

    gravity = True
    gravity_speed = 0
    g = 5


    def __init__(self,picture,x,y):
        sprite.Sprite.__init__(self)

        self.picture = transform.scale(image.load(picture), (100,100))

        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rect.bottom = self.rect.y-100
        self.rect.top = self.rect.y


    def update(self,person, wall1,wall2):
        if self.gravity:
            self.gravity_speed += self.g
            self.rect.y += self.gravity_speed
            pass
        else:
            self.gravity_speed -= self.g
            self.rect.y +=self.gravity_speed

        if sprite.collide_rect(wall1,person):
            self.rect.top = wall1.rect.bottom
            self.gravity_speed = 0

        elif sprite.collide_rect(wall2,person):
            self.rect.bottom = wall2.rect.top
            self.gravity_speed = 0










    def reset(self,win):
        win.blit(self.picture, (self.rect.x,self.rect.y))

    '''def update(self):
        keys = key.get_pressed()

        if keys[K_d]:
            self.rect.x += 20
            self.up = False
            self.right = True
            self.down = False
            self.left = False
            if sprite.collide_rect(cowboy, wall_horisontal1) or sprite.collide_rect(cowboy, wall_horisontal2) or sprite.collide_rect(cowboy,wall_horisontal3) or sprite.collide_rect(cowboy, wall_horisontal4) or sprite.collide_rect(cowboy, wall_vertical1) or sprite.collide_rect(cowboy, wall_vertical2) or sprite.collide_rect(cowboy,wall_vertical3) or sprite.collide_rect(cowboy,wall_vertical4):

                if cowboy.right:
                    cowboy.rect.x -= 20

        if keys[K_a]:
            self.rect.x -= 20
            self.up = False

            self.right = False
            self.down = False
            self.left = True
            if sprite.collide_rect(cowboy, wall_horisontal1) or sprite.collide_rect(cowboy,
                                                                                    wall_horisontal2) or sprite.collide_rect(
                    cowboy, wall_horisontal3) or sprite.collide_rect(cowboy, wall_horisontal4) or sprite.collide_rect(
                    cowboy, wall_vertical1) or sprite.collide_rect(cowboy, wall_vertical2) or sprite.collide_rect(
                    cowboy, wall_vertical3) or sprite.collide_rect(cowboy, wall_vertical4):
                if cowboy.left:
                    cowboy.rect.x += 20

        if keys[K_w]:
            self.rect.y -= 20
            self.up = True
            self.right = False
            self.down = False
            self.left = False
            if sprite.collide_rect(cowboy, wall_horisontal1) or sprite.collide_rect(cowboy, wall_horisontal2) or sprite.collide_rect(cowboy,wall_horisontal3) or sprite.collide_rect(cowboy, wall_horisontal4) or sprite.collide_rect(cowboy, wall_vertical1) or sprite.collide_rect(cowboy, wall_vertical2) or sprite.collide_rect(cowboy,wall_vertical3) or sprite.collide_rect(cowboy,wall_vertical4):
                if cowboy.up:
                    cowboy.rect.y += 20

        if keys[K_s]:
            self.rect.y += 20
            self.up = False
            self.right = False
            self.down = True
            self.left = False
            if sprite.collide_rect(cowboy, wall_horisontal1) or sprite.collide_rect(cowboy, wall_horisontal2) or sprite.collide_rect(cowboy,wall_horisontal3) or sprite.collide_rect(cowboy, wall_horisontal4) or sprite.collide_rect(cowboy, wall_vertical1) or sprite.collide_rect(cowboy, wall_vertical2) or sprite.collide_rect(cowboy,wall_vertical3) or sprite.collide_rect(cowboy,wall_vertical4):
                if cowboy.down:
                    cowboy.rect.y -= 20'''

    def reset(self,win):
        win.blit(self.picture, (self.rect.x,self.rect.y))