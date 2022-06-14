import pygame
import sys
from Button import Button
import Menu
import Platformer
WINWIDTH,WINHEIGHT = 600,400
pygame.init()
WIN = pygame.display.set_mode((WINWIDTH,WINHEIGHT))
Back2MenuImg = pygame.image.load("Images/menu.png")
BackGroundImg = pygame.image.load("Images/backgroundimg.png")
ResumeImg = pygame.image.load("Images/resumebutton.png")
ResumeButton = Button((WINWIDTH/2)-64,100,ResumeImg,128,64)
Back2MenuButton = Button((WINWIDTH/2)-64,200,Back2MenuImg,128,64)
def set_text(string, coordx, coordy, fontSize): #Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    #(0, 0, 0) is black, to make black text
    text = font.render(string, True, (255,255,255)) 
    textRect = text.get_rect()
    textRect.center = (coordx, coordy) 
    return (text, textRect)

def Draw():
    WIN.blit(BackGroundImg, (0,0))
    Back2MenuButton.Draw(WIN)
    ResumeButton.Draw(WIN)
    totalText = set_text("Paused...",300, 50, 40)
    WIN.blit(totalText[0], totalText[1])
    pygame.display.update()
def Main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        Draw()
        if Back2MenuButton.CheckClick():
            Menu.Main()
        if ResumeButton.CheckClick():
            Platformer.Main()
if __name__ == "__main__":
    Main()
