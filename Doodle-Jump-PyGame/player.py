import pygame
from settings import *
vec=pygame.math.Vector2
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_pikachu_sprite=pygame.sprite.Sprite()
        self.img_pikachu_sprite.image = pygame.image.load('pikachu.png').convert()
        self.img_pikachu_sprite.rect=self.img_pikachu_sprite.image.get_rect()
        self.img_pikachu1 = pygame.sprite.Sprite()
        self.img_pikachu1.image = pygame.image.load('pikachu1.png').convert_alpha()
        self.img_pikachu1.rect = self.img_pikachu1.image.get_rect()
        self.pos = vec(display_width / 2, display_height - 100)
        self.img_pikachu_sprite.rect.topleft =[self.pos.x,self.pos.y]
        self.img_pikachu1.rect.topleft = [self.pos.x, self.pos.y]
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.mask_image = pygame.mask.from_surface(self.img_pikachu_sprite.image)
        #return img_pikachu_sprite

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

