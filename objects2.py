import pygame
import os
from config2 import *

scale=4
#1 = right
class Entity(pygame.sprite.Sprite):
    def __init__(self, pic, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.pic = pic
        self.speed = speed
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.air = True
        self.jump_a = False
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        
        animation_types = ['idle', 'run', 'jump']
        for animation in animation_types:
            temp_list = []
            num_of_frames = len(os.listdir(f'assets/{self.pic}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f"assets/{self.pic}/{animation}/{i}.png")
                img = pygame.transform.scale(img, (int(img.get_width() / scale), int(img.get_width() / scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)
        #temp_list = []
        
        #for i in range(3):
        #    img = pygame.image.load(f"assets/{self.pic}/run/{i}.png")
        #    img = pygame.transform.scale(img, (int(img.get_width() / scale), int(img.get_width() / scale)))
        #    temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.prect = self.image.get_rect()
        self.prect.center = (x, y)
        
        
    def move(self, moving_left, moving_right):
        sx = 0
        sy = 0
        if moving_left:
            sx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            sx = self.speed
            self.flip = False
            self.direction = 1

        
        if self.jump == True and self.air == False:
            self.vel_y = -10
            self.jump = False
            self.air = True
            self.jump_a = True
        
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        sy += self.vel_y
        
        
        if self.prect.bottom + sy > 600:
            sy = 600 - self.prect.bottom
            self.air = False
            self.jump_a = False
        self.prect.x += sx
        self.prect.y += sy    
    
    def update_animation(self):
        ANIMATION_SPEED = 50
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_SPEED:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
            
    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
            
    
    
    def draw(self):
        screen.blit(pygame.transform.flip(self.image,self.flip, False), self.prect)