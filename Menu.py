
import pygame
import sys
from Button import Button
import Platformer
# BACKGROUND
WINWIDTH,WINHEIGHT = 600,400
pygame.init()
WIN = pygame.display.set_mode((WINWIDTH,WINHEIGHT))
pygame.display.set_caption('CRINEMAFT')
background_img = pygame.image.load('Images/backgroundimg.png')
PlayButtonImage = pygame.image.load('Images/PlayButton.png')
PlayButton = Button((WINWIDTH/2)-64,100,PlayButtonImage,128,64)
def set_text(string, coordx, coordy, fontSize): #Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    #(0, 0, 0) is black, to make black text
    text = font.render(string, True, (255,255,255)) 
    textRect = text.get_rect()
    textRect.center = (coordx, coordy) 
    return (text, textRect)

def Draw():
    WIN.blit(background_img, (0,0))
    PlayButton.Draw(WIN)
    totalText = set_text("Crine Maft",300, 50, 40)
    controlsText = set_text("Arrow Keys to move,",300, 200, 20)
    controlsText1 = set_text("space to jump," ,300, 250, 20)
    controlsText2 = set_text("right and left click to place and destroy blocks," ,300, 300, 20)
    WIN.blit(totalText[0], totalText[1])
    WIN.blit(controlsText[0], controlsText[1])
    WIN.blit(controlsText1[0], controlsText1[1])
    WIN.blit(controlsText2[0], controlsText2[1])
    pygame.display.update()

def Main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Platformer.Main()
            
        
        Draw()
        if PlayButton.CheckClick():
            Platformer.Main()
if __name__ == "__main__":
    Main()