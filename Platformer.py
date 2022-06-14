from tkinter import W
import pygame, sys
import numpy as np
import escapeMenu
Currblock = '1'
clock = pygame.time.Clock()
player_x_block=0
player_y_block=0
from pygame.locals import *
pygame.init() # initiates pygame

pygame.display.set_caption('CRINEMAFT')

WINDOW_SIZE = (600,400)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window

display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled

moving_right = False
moving_left = False
vertical_momentum = 0
air_timer = 0

true_scroll = [0,0]

def load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

game_map = load_map('map')

grass_img = pygame.image.load('Images/grass.png')
dirt_img = pygame.image.load('Images/dirt.png')
flower_img = pygame.image.load('Images/flower.png')
flower_img.set_colorkey((0,0,0))

planks_img = pygame.image.load('Images/planks.png')
spruceplanks_img = pygame.image.load('Images/spruceplank.png')
spruce_wood_img = pygame.image.load('Images/sprucewood.png')
cobble_img = pygame.image.load('Images/cobble.png')
leaves_png = pygame.image.load('Images/leaves.png')
leaves_png.set_colorkey((0,0,0))

planks_img = pygame.image.load('Images/planks.png')
stone_img = pygame.image.load('Images/stone.png')
wood_img = pygame.image.load('Images/wood.png')
player_img = pygame.image.load('Images/player.png').convert()
player_img.set_colorkey((255,255,255))

player_rect = pygame.Rect(100,100,5,13)

background_objects = [[0.25,[120,10,70,400]],[0.25,[280,30,40,400]],[0.5,[30,40,40,400]],[0.5,[130,90,100,400]],[0.5,[300,80,120,400]]]

def collision_test(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect,movement,tiles):
    collision_types = {'top':False,'bottom':False,'right':False,'left':False}
    rect.x += movement[0]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

def Main(): 
    # Globals
    global player_x_block
    global player_y_block
    global Currblock
    global true_scroll
    global air_timer
    global moving_right
    global moving_left
    global vertical_momentum
    global player_rect
    global game_map
    global background_objects
    global screen
    global display
    global grass_img
    global dirt_img
    global flower_img
    global planks_img
    global spruceplanks_img
    global spruce_wood_img
    global cobble_img
    global leaves_png
    global stone_img
    global wood_img
    global player_img
    # game loop
    while True:
        display.fill((146,244,255)) # clear screen by filling it with blue

        true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20
        true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        pygame.draw.rect(display,(7,80,75),pygame.Rect(0,120,300,80))
        for background_object in background_objects:
            obj_rect = pygame.Rect(background_object[1][0]-scroll[0]*background_object[0],background_object[1][1]-scroll[1]*background_object[0],background_object[1][2],background_object[1][3])
            if background_object[0] == 0.5:
                pygame.draw.rect(display,(14,222,150),obj_rect)
            else:
                pygame.draw.rect(display,(9,91,85),obj_rect)

        tile_rects = []
        y = 0
        for layer in game_map:
            x = 0
            for tile in layer:
                if tile == '1':
                    display.blit(dirt_img,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '2':
                    display.blit(grass_img,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '3':
                    display.blit(flower_img,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '4':
                    display.blit(planks_img,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '5':
                    display.blit(spruceplanks_img,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '6':
                    display.blit(cobble_img,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '7':
                    display.blit(leaves_png,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '8':
                    display.blit(stone_img,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '9':
                    display.blit(wood_img,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'p':
                    display.blit(spruce_wood_img,(x*16-scroll[0],y*16-scroll[1]))
                if tile != '0':
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                x += 1
            y += 1
        ## Hotbar
        pygame.draw.rect(display,(40,40,40),pygame.Rect(50,180,200,20))
        if Currblock == 'p':
            Currblockhotbar = '10'
        else:
            Currblockhotbar = Currblock
        pygame.draw.rect(display,(200,200,0),pygame.Rect((int(Currblockhotbar)*18)+40,181,20,18))
        display.blit(dirt_img,(60,183))
        display.blit(grass_img,(78,183))
        display.blit(flower_img,(96,183))
        display.blit(planks_img,(114,183))
        display.blit(spruceplanks_img,(132,183))
        display.blit(cobble_img,(150,183))
        display.blit(leaves_png,(168,183))
        display.blit(stone_img,(186,183))
        display.blit(wood_img,(204,183))
        display.blit(spruce_wood_img,(222,183))


        player_movement = [0,0]
        if moving_right == True:
            player_movement[0] = 2
            player_x_block+=2
        if moving_left == True:
            player_movement[0] -= 2
            player_x_block -=2
        player_movement[1] += vertical_momentum
        vertical_momentum += 0.2
        if vertical_momentum > 3:
            vertical_momentum = 3

        player_rect,collisions = move(player_rect,player_movement,tile_rects)

        if collisions['bottom'] == True:
            air_timer = 0
            vertical_momentum = 0
        else:
            air_timer += 1

        display.blit(player_img,(player_rect.x-scroll[0],player_rect.y-scroll[1]))

        for event in pygame.event.get(): # event loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    moving_right = True
                if event.key == K_LEFT:
                    moving_left = True
                if event.key == K_UP:
                    if air_timer < 6:
                        vertical_momentum = -5
                if event.key == K_1:
                    Currblock = '1'
                if event.key == K_2:
                    Currblock = '2'
                if event.key == K_3:
                    Currblock = '3'
                if event.key == K_4 :
                    Currblock = '4'
                if event.key == K_5:
                    Currblock = '5'
                if event.key == K_6:
                    Currblock = '6'
                if event.key == K_7 :
                    Currblock = '7'
                if event.key == K_8 :
                    Currblock = '8'
                if event.key == K_9:
                    Currblock = '9'
                if event.key == K_0:
                    Currblock = 'p'
                if event.key == K_ESCAPE:
                    escapeMenu.Main()
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_LEFT:
                    moving_left = False
        ## Placing and breaking
        weird_glitch_offset = -32
        scroll_offset_x=-100
        scroll_offset_y=-100
        player_y_block=player_rect.y-99
        
        if pygame.mouse.get_pressed()[2] == True:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pos = np.asarray(mouse_pos)
            mouse_pos[0]+=player_x_block
            mouse_pos[1]+=player_rect.y-99
            x_tile = int(((mouse_pos[1]+scroll[1]+weird_glitch_offset)/32))
            y_tile = int(((mouse_pos[0]-32+scroll[0]+player_y_block+weird_glitch_offset)/32))
        
            if game_map[x_tile][y_tile]=='0':
                game_map[x_tile][y_tile] = Currblock
            print(Currblock)
        if pygame.mouse.get_pressed()[0]==True:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pos = np.asarray(mouse_pos)
            mouse_pos[0]+=player_x_block
            mouse_pos[1]+=player_rect.y-99
            x_tile = int(((mouse_pos[1]+scroll[1]+weird_glitch_offset)/32))
            y_tile = int(((mouse_pos[0]-32+scroll[0]+player_y_block+weird_glitch_offset)/32))
        
            game_map[x_tile][y_tile] = '0'
        screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
        pygame.display.update()
        clock.tick(60)
if __name__ == "__main__":
    Main()