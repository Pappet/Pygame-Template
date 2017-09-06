import pygame, sys, random, Color, Utilitys, Settings


class Game:
    # Initialise The Game
    def __init__(self):
        # Initialise Pygame and the Sound Mixer
        pygame.init()
        pygame.mixer.init()
        self.load_data()
        # Generate a Screen to Display stuff
        if Settings.Fullscreen:
            Settings.ScreenWidth, Settings.ScreenHeight = pygame.display.list_modes()[0]
            self.screen = pygame.display.set_mode((Settings.ScreenWidth, Settings.ScreenHeight), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((Settings.ScreenWidth, Settings.ScreenHeight), pygame.RESIZABLE)
        # Set the Window Name
        pygame.display.set_caption(Settings.Title)
        # Load Icon
        pygame.display.set_icon(self.icon)
        # Load a Font
        self.font = pygame.font.match_font(Settings.FONT)
        # Initialise the Clock to limit the Gamespeed
        self.clock = pygame.time.Clock()
        # Is the Game running
        self.running = True
        # Is the game paused
        self.paused = False
        # Group for all Sprites
        # Do i need this???
        self.all_sprites = pygame.sprite.Group()

    # Generates an new Game
    # Must reset Variables and stuff
    def new(self):
        self.run()

    def load_data(self):
        self.icon = pygame.image.load(Settings.Icon)
        self.start_sound = pygame.mixer.Sound(Settings.StartSound)
        self.pause_sound = pygame.mixer.Sound(Settings.PauseSound)

    # The Whole Game
    # Does it need anything else?
    def run(self):
        # Show the Start Screen
        self.start_screen()
        # THE GAMELOOP
        while self.running:
            self.clock.tick(Settings.FPS)
            self.events()
            self.update()
            self.render()
        # Show something when the Game is closing
        self.end_screen()
        # Close the Game
        self.close()

    # The Events, like Key pressed and stuff
    def events(self):
        # Get all Events
        for event in pygame.event.get():
            # What happens when you click the little X in the upper right corner
            if event.type == pygame.QUIT:
                self.running = False
                break
            if event.type == pygame.FULLSCREEN:
                print("Pressed Fullscreen Button")
            if event.type == pygame.KEYDOWN:
                # What happens when you click the Escape Key
                if event.key == pygame.K_ESCAPE:
                    # Pause the Game
                    self.paused = True

    # Here comes the Gamemechanics
    def update(self):
        if not self.paused:
            pass
        else:
            pass

    # Rendering the Stuff on the Screen
    def render(self):
        # Check if the Game is paused
        if not self.paused:
            # if not render the normal Game stuff
            # Reset the screen to all black
            self.screen.fill(Color.Black)
            # Just for Testing
            Utilitys.drawText("GAME", 128, Color.Green, Settings.ScreenWidth / 2, Settings.ScreenHeight / 2, self.screen)
        else:
            # if its paused render the Pause Screen
            self.pause_screen()
        # needed for double Buffering
        pygame.display.flip()

    # Close The Game
    def close(self):
        # Shutdown Pygame and Sys
        pygame.quit()
        sys.exit()

    # Basic Start Screen with Text Info's
    def start_screen(self):
        # Play a Sound
        self.start_sound.play()
        self.screen.fill(Color.Black)
        # Write Some Text
        Utilitys.drawText("START", 128, Color.White, Settings.ScreenWidth / 2, Settings.ScreenHeight / 2, self.screen)
        pygame.display.flip()
        # Waiting until Player presses a Key to Continue
        Utilitys.wait_for_key(self, self.paused)

    # Basic End Screen with Text Info's
    def end_screen(self):
        self.screen.fill(Color.Black)
        # Write Some Text
        Utilitys.drawText("Thank you for playing!", 64, Color.Red, Settings.ScreenWidth / 2, Settings.ScreenHeight / 4, self.screen)
        Utilitys.drawText("press any Key to close", 32, Color.Red, Settings.ScreenWidth / 2, Settings.ScreenHeight / 2, self.screen)
        pygame.display.flip()
        # Waiting until Player presses a Key to Continue
        Utilitys.wait_for_key(self, self.paused)

    # Basic Pause Screen with Text Info's
    def pause_screen(self):
        self.pause_sound.play()
        # Draw an transparent Background over everything else
        transparentBackground = pygame.Surface((Settings.ScreenWidth, Settings.ScreenHeight))
        transparentBackground.set_alpha(128)
        transparentBackground.fill(Color.Black)
        self.screen.blit(transparentBackground, (0, 0))
        # Write Some Text
        Utilitys.drawText("Pause",
                          64,
                          Color.RandomColor(),
                          Settings.ScreenWidth / 2,
                          10,
                          self.screen)
        Utilitys.drawText("Press any Key to Continue...", 32,
                          Color.RandomColor(),
                          Settings.ScreenWidth / 2,
                          76,
                          self.screen)
        Utilitys.drawText("Press Escape to Quit", 32,
                          Color.RandomColor(),
                          Settings.ScreenWidth / 2,
                          Settings.ScreenHeight - 32,
                          self.screen)
        pygame.display.flip()
        # Waiting until Player presses a Key to Continue
        Utilitys.wait_for_key(self, self.paused)
        # End the pause
        self.paused = False
