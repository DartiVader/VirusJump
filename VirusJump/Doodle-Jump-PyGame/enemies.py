import pygame
from settings import *
from spritesheets import *
import random
dic_mobs = {1: [[566, 510, 122, 139], [568, 1543, 122, 135]],
                2: [[400, 510, 122, 139],[400, 660, 122, 100]],
                3: [[805, 615, 120, 130], [800, 862, 120, 130]],
                4: [[420, 1684, 150, 150], [412, 1885, 150, 150]],
                5: [[740, 1083, 100, 125], [708, 1264, 100, 138]],
                6: [[46, 1463, 120, 91], [32, 1560, 110, 90]],
                7: [[419, 1541, 140, 85], [419, 1541, 140, 85]]} #словарь с координатами и ш/в мобов из spritesheet


class Enemies(pygame.sprite.Sprite):

    def __init__(self,game):
        global dic_mobs
        n = random.randint(1,7)
        self.groups=game.enemies
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.enemyNum_ = n
        self.spritesheetsobj = SpriteSheet()
        self.image_up = self.spritesheetsobj.imageLoad(dic_mobs[n][0][0], dic_mobs[n][0][1], dic_mobs[n][0][2],
                                                       dic_mobs[n][0][3])
        # self.image_up = pygame.image.load('meowth1.png').convert()
        # self.image_up = pygame.transform.scale(self.image_up, (221 // 3, 240 // 3))
        self.image_up.set_colorkey(black)
        self.image_down = self.spritesheetsobj.imageLoad(dic_mobs[n][1][0], dic_mobs[n][1][1], dic_mobs[n][1][2],
                                                         dic_mobs[n][1][3])
        #self.image_down = pygame.image.load('meowth2.png').convert()
        #self.image_down = pygame.transform.scale(self.image_down, (286 // 3, 240 // 3))
        self.image_down.set_colorkey(black)
        self.image=self.image_up
        self.rect=self.image.get_rect()
        self.rect.centerx=random.choice([-100,display_width+100])
        self.vx=random.randrange(1,4)
        if self.rect.centerx>display_width:
            self.vx=-self.vx
        self.rect.y = int(random.randrange(0, int(display_height/2)))
        self.vy=0
        self.dy=0.5
        print("enemy")

    def update(self):
        self.rect.x+=self.vx
        self.vy+=self.dy
        if self.vy>3 or self.vy<-3:
            self.dy=-self.dy
        center=self.rect.center
        if self.dy<0:
            self.image=self.image_up
        else:
            self.image=self.image_down
        self.rect=self.image.get_rect()
        self.mask_image = pygame.mask.from_surface(self.image)
        self.rect.center=center
        self.rect.y+=self.vy
        if self.rect.left>display_width+100 or self.rect.right<-100:
            self.kill()