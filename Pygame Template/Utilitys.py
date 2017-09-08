import pygame
from Settings import *

#An Class to Groupe small but usefull functions
#Use it with:
#   Utilitys.drawText(...)
#   Utilitys.wait_for_key(...)

#To Draw text on the screen
def drawText(text, size, color, x, y, screen):
    font = pygame.font.Font(FONT,size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

#Make the Game wait till the Player pressed a Key
def wait_for_key(self, paused):
    waiting = True
    while waiting:
        self.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                waiting = False