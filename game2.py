import pygame
from config2 import *
from objects2 import *

pygame.init()
pygame.display.set_caption("Provoked Penguin")
game_clock = pygame.time.Clock()



moving_left = False     #sets_some_stuff_up_so_it_doesnt_do_anything
moving_right = False
moving_up = False
shoot = False
#colours
BG =(144, 201, 120)
RED = (255, 0, 0)

#temp_ground
def draw_bg():
    screen.fill(BG)
    pygame.draw.line(screen, RED, (0, 600), (SCREEN_WIDTH, 600))

player = Entity('player', 200, 200, 4, 5)   #calls_entity_as_player_tells_where_to_call_sprite_from_and_sizes_of_rec_and_scale_and_speed
enemy = Entity('enemy', 200, 200, 4, 5)     #calls_entity_as_enemy_tells_where_to_call_sprite_from_and_sizes_of_rec_and_scale_and_speed


running = True
while running:  #main_game_loop
    game_clock.tick(FPS)
    draw_bg()
    player.draw()
    enemy.draw()
    if player.alive:    #checks_if_player_is_still_alive_if_not_stops_all_movement_and_sprite_changes
        if player.jump_a:
            player.update_action(2)#2: jump
        elif moving_left or moving_right:
            player.update_action(1)#1: run
        else:
            player.update_action(0)#0: idle
            
    
        player.move(moving_left, moving_right)
    player.update_animation()

    for event in pygame.event.get():
        #quit_game
        if event.type == pygame.QUIT:
            running = False
        #controls_i_geuss
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w and player.alive: #makes_sure_player_is_dead_so_no_jump_when dead
                player.jump = True
            if event.key == pygame.K_SPACE:
                player.alive = False
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_SPACE:
                player.alive = True
            
    
    pygame.display.update()
pygame.quit()