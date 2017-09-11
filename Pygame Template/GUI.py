import pygame
import Color
import Settings


class Button(object):
    def __init__(self, text, size, x, y, width=None):
        # tracks the state of the button
        self.buttonDown = False  # is the button currently pushed down?
        self.buttonPressed = False
        self.mouseOverButton = False  # is the mouse currently hovering over the button?
        self._visible = True  # is the button visible

        self.clickSound = pygame.mixer.Sound(Settings.ClickSound)

        self.buttonColor = Color.LightGray
        self.highlightColor = Color.Gray
        self.pressedColor = Color.DarkGray
        self.textColor = Color.Black

        self.text = text
        self.size = size
        self.font = pygame.font.Font(Settings.FONT, self.size)
        self.text_surface = self.font.render(self.text, True, self.textColor)

        self.pos = (x, y)
        if width:
            self.width = width
        else:
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
        click = pygame.mouse.get_pressed()

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.mouseOverButton = True
            ret_val.append("over")
            if click[0] == 1 and not self.buttonDown:
                self.buttonDown = True
                self.clickSound.play()
                ret_val.append("clicked")
            elif click[0] == 0:
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


def button_grid(titles, size, pos=None):
    font = pygame.font.Font(Settings.FONT, size)
    buttons = []

    for index, item in enumerate(titles):
        if font.size(item)[0] > Settings.ScreenWidth / len(titles):
            fiting = True
        else:
            fiting = False
        while fiting:
            size -= 2
            font = pygame.font.Font(Settings.FONT, size)
            if font.size(item)[0] < Settings.ScreenWidth / len(titles):
                fiting = False

    if pos == "Bottom":
        y = Settings.ScreenHeight - font.size(titles[0])[1]
    else:
        y = 0

    for index, item in enumerate(titles):
        offset = index * (Settings.ScreenWidth / len(titles))
        buttons.append(Button(item, size, offset, y, Settings.ScreenWidth / len(titles)))
        buttons[index].rect.topleft = (offset, y)

    return buttons
