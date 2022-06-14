import pygame

class Button:
    def __init__(self, x, y, image, scaleX, scaleY):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (scaleX, scaleY))
        self.initialimage = pygame.transform.scale(image, (scaleX, scaleY))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False
        self.Action = False
        self.Hover = False

    def Draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def CheckClick(self):
        action = False
        # get mouse position
        self.pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(self.pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action

    def CheckHover(self):
        self.pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(self.pos):
            pass
        else:
            self.Hover = False
            self.image = self.initialimage
        if self.rect.collidepoint(self.pos) and self.Hover == False:
            self.image = self.hoverimage
            self.Hover = True
        return self.Hover
