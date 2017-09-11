import pygame
import Color
import Settings


class Button(object):
    def __init__(self, text, size, x, y):
        # tracks the state of the button
        self.buttonDown = False  # is the button currently pushed down?
        self.mouseOverButton = False  # is the mouse currently hovering over the button?
        self._visible = True  # is the button visible

        self.buttonColor = Color.LightGray
        self.highlightColor = Color.Gray
        self.pressedColor = Color.DarkGray
        self.textColor = Color.Black

        self.text = text
        self.size = size
        self.font = pygame.font.Font(Settings.FONT, self.size)
        self.text_surface = self.font.render(self.text, True, self.textColor)

        self.pos = (x, y)
        self.width = self.text_surface.get_width() + 20
        self.height = self.text_surface.get_height()

        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.width / 2, self.height / 2)

        self.imageNormal = pygame.Surface((self.width, self.height))
        self.imageNormal.fill(self.buttonColor)

        pygame.draw.rect(self.imageNormal, Color.Black, pygame.Rect((0, 0, self.width, self.height)), 1)
        pygame.draw.line(self.imageNormal, Color.White, (1, 1), (self.width - 2, 1))
        pygame.draw.line(self.imageNormal, Color.White, (1, 1), (1, self.height - 2))
        pygame.draw.line(self.imageNormal, Color.DarkGray, (1, self.height - 2), (1, 1))
        pygame.draw.line(self.imageNormal, Color.DarkGray, (1, 1), (self.width - 2, 1))
        pygame.draw.line(self.imageNormal, Color.Gray, (2, self.height - 3), (2, 2))
        pygame.draw.line(self.imageNormal, Color.Gray, (2, 2), (self.width - 3, 2))

        self.imagePressed = pygame.Surface((self.width, self.height))
        self.imagePressed.fill(self.pressedColor)

        pygame.draw.rect(self.imagePressed, Color.Black, pygame.Rect((0, 0, self.width, self.height)), 1)
        pygame.draw.line(self.imagePressed, Color.White, (1, 1), (self.width - 2, 1))
        pygame.draw.line(self.imagePressed, Color.White, (1, 1), (1, self.height - 2))
        pygame.draw.line(self.imagePressed, Color.DarkGray, (1, self.height - 2), (1, 1))
        pygame.draw.line(self.imagePressed, Color.DarkGray, (1, 1), (self.width - 2, 1))
        pygame.draw.line(self.imagePressed, Color.Gray, (2, self.height - 3), (2, 2))
        pygame.draw.line(self.imagePressed, Color.Gray, (2, 2), (self.width - 3, 2))

        self.imageHighlight = pygame.Surface((self.width, self.height))
        self.imageHighlight.fill(self.highlightColor)

        pygame.draw.rect(self.imageHighlight, Color.Black, pygame.Rect((0, 0, self.width, self.height)), 1)
        pygame.draw.line(self.imageHighlight, Color.White, (1, 1), (self.width - 2, 1))
        pygame.draw.line(self.imageHighlight, Color.White, (1, 1), (1, self.height - 2))
        pygame.draw.line(self.imageHighlight, Color.DarkGray, (1, self.height - 2), (1, 1))
        pygame.draw.line(self.imageHighlight, Color.DarkGray, (1, 1), (self.width - 2, 1))
        pygame.draw.line(self.imageHighlight, Color.Gray, (2, self.height - 3), (2, 2))
        pygame.draw.line(self.imageHighlight, Color.Gray, (2, 2), (self.width - 3, 2))

        self.rect = self.imageNormal.get_rect()
        self.rect.center = self.pos

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

def ButtonGrid(titles, size, pos):
    font = pygame.font.Font(Settings.FONT, size)
    buttons = []
    offset =  0 + font.size(titles[0])[0] / 2
    y = 0


    for index, item in enumerate(titles):
        if pos == "Top":
            y = 0 + font.size(item)[1] / 2
            offset += Settings.ScreenWidth / len(titles) * index + font.size(item)[0] / 2
        if pos == "Bottom":
            y = Settings.ScreenHeight - size
            offset = Settings.ScreenHeight / len(titles)

        buttons.append(Button(item, size, offset, y))

    return buttons


