import pygame
import Settings
import Color


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(Color.Green)
        self.rect = self.image.get_rect()
        self.rect.center = (Settings.ScreenWidth / 2, Settings.ScreenHeight / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > Settings.ScreenWidth:
            self.rect.left = 0
