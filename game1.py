import pygame
from pygame.locals import *
from config import *
from objects1 import *
from random import randint


def game1():
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Street Runner')


    game_clock = pygame.time.Clock()

    #sprite groups
    all_sprites = pygame.sprite.Group()
    players = pygame.sprite.Group()
    monsters = pygame.sprite.Group()
    coins = pygame.sprite.Group()

    #player object
    player = Player((0,WINDOW_HEIGHT/2),60,100)
    player.add(all_sprites,players)
    player.vel = Vector2(2,0)

    #create 5 monsters in random positions
    # on the right edge of the screen moving left
    for n in range(5):
        new_monster = Monster((WINDOW_WIDTH,randint(0,WINDOW_HEIGHT)),50,50)
        new_monster.add(all_sprites,monsters)
        new_monster.vel = Vector2(-5,0)
        
    def pause():
        paused = True
        while paused:
            event = pygame.event.wait()
            if event.type == KEYDOWN:
                if event.key == K_p:
                    paused = False
        
    #main game loop

    running = True
    while running:

        game_clock.tick(FPS)

        #get the events
        events = pygame.event.get()

        #loop through all the events
        for event in events:
            print(event)
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_SPACE:
                    player.jump()
                elif event.key == K_LEFT:
                    player.move("left")
                elif event.key == K_RIGHT:
                    player.move("right")
        for monster in monsters:
            if not window.get_rect().inflate(100,100).contains(monster.rect):
                monster.kill()
                new_monster = Monster((WINDOW_WIDTH,randint(0,WINDOW_HEIGHT)),50,50)
                new_monster.add(all_sprites,monsters)
                new_monster.vel = Vector2(-5,0)

        hit_monsters = pygame.sprite.spritecollide(player,monsters,True)
        if len(hit_monsters) != 0:
            new_monster = Monster((WINDOW_WIDTH,randint(0,WINDOW_HEIGHT)),50,50)
            new_monster.add(all_sprites,monsters)
            new_monster.vel = Vector2(-5,0)
        all_sprites.update()
        window.fill((40,40,250))
        for sprite in all_sprites:
            window.blit(sprite.image,sprite.rect)
        pygame.display.update()

    pygame.quit()