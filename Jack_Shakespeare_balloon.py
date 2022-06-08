import os
import random
import pygame
import math
import sys
from pygame.locals import *
from sys import exit

surface = pygame.display.set_mode((400,300));
bullet_colour = (255,0,0);
balloon_colour = (0,0,255);
cannon_colour = (0,255,0);

pygame.display.set_caption("Balloon game");
clock = pygame.time.Clock();
missed = 0;
hit = 0;
bullet_list = [];
print("Using pygame version pygame-2.1.2");

class Bullet(object):
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        
    def move(self, surface):
        self.x -= 20;
        self.rect = pygame.draw.rect(surface, bullet_colour, (self.x-10, self.y+22, 15, 5));
        

class Cannon(object):
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        

    def handle_keys(self):
        pressed = False;
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP):
                    self.y -= 8;
                    
                if (event.key == pygame.K_DOWN):
                    self.y += 8;
                    
                if (event.key == pygame.K_SPACE):
                    bullet = Bullet(self.x, self.y);
                    bullet_list.append(bullet);
            if event.type == pygame.QUIT:
                pygame.quit()


                    
        
    def draw(self, surface):
        pygame.draw.rect(surface, cannon_colour, (self.x-10, self.y+20, 10, 10));
        pygame.draw.rect(surface, cannon_colour, (self.x, self.y, 10, 50));
        
                
class Balloon(object):
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        
    def move(self, surface, dir):
        if self.y > 10 and self.y + dir < 290:
            self.y += dir;
            
        elif self.y <= 10:
            self.y = 290; 
            
        elif self.y >= 290:
            self.y = 10;
            
        self.rect = pygame.draw.circle(surface, balloon_colour, (self.x, self.y), 5);

pygame.init()

cannon = Cannon(380,150);
balloon = Balloon(20, 20);
running = True;
dir = 2;

while running:

    rand = random.randint(0, 20);
    surface.fill((0, 0, 0));
 
    for bullet in bullet_list:
        bullet.move(surface);
        if bullet.rect.colliderect(balloon.rect):
            hit += 1;
            bullet_list.remove(bullet);
        if bullet.x < 0:
            missed += 1;
            bullet_list.remove(bullet);
        
    cannon.draw(surface);
    cannon.handle_keys()

    if (rand == 10):
        dir = dir*-1;
        
    balloon.move(surface, dir);
    
    if hit > 0:
        surface.fill((0, 0, 0));
        sysfont = pygame.font.get_default_font()
        font = pygame.font.SysFont(None, 48)
        img = font.render("Hit! You missed:", True, (255,0,0))
        rect = img.get_rect()
        font1 = pygame.font.SysFont('chalkduster.ttf', 72)
        img1 = font1.render(str(missed) , True, (0,0,255))
        surface.blit(img, (20, 20))
        surface.blit(img1, (20, 50))
        running = False;

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False 

    pygame.display.update();

    clock.tick(60);
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

