import pygame
import Color
import Settings


class Button(object):
    def __init__(self, text, size, x, y):
        # tracks the state of the button
        self.buttonDown = False  # is the button currently pushed down?
        self.mouseOverButton = False  # is the mouse currently hovering over the button?
        self._visible = True  # is the button visible

        self.text = text
        self.size = size
        self.font = pygame.font.Font(Settings.FONT, self.size)

        self.buttonColor = Color.LightGray
        self.highlightColor = Color.Gray
        self.pressedColor = Color.DarkGray
        self.textColor = Color.Black

        self.pos = (x, y)
        self.width = self.font.size(text)[0]
        self.height = self.font.size(text)[1]

        self.imageNormal = pygame.Surface((self.width, self.height))
        self.imageNormal.fill(self.buttonColor)

        self.imagePressed = pygame.Surface((self.width, self.height))
        self.imagePressed.fill(self.pressedColor)

        self.imageHighlight = pygame.Surface((self.width, self.height))
        self.imageHighlight.fill(self.highlightColor)

        self.rect = self.imageNormal.get_rect()
        self.rect.center = self.pos

        self.text_surface = self.font.render(self.text, True, self.textColor)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = (self.width / 2, 0 + self.height * 0.1)

    def handle_events(self):
        ret_val = []

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.mouseOverButton = True
            if pygame.mouse.get_pressed()[0]:
                self.buttonDown = True
                ret_val.append("clicked")
            else:
                self.buttonDown = False
        else:
            self.buttonDown = False
            self.mouseOverButton = False

        return ret_val

    def draw(self, screen):
        if self._visible:
            if self.buttonDown:
                self.imagePressed.blit(self.text_surface, self.text_rect)
                screen.blit(self.imagePressed, self.rect)
            elif self.mouseOverButton:
                self.imageHighlight.blit(self.text_surface, self.text_rect)
                screen.blit(self.imageHighlight, self.rect)
            else:
                self.imageNormal.blit(self.text_surface, self.text_rect)
                screen.blit(self.imageNormal, self.rect)

    def update(self):
        pass
