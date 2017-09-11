import pygame
import sys
import Settings
import Scenes


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
        # Initialise the Clock to limit the Gamespeed
        self.clock = pygame.time.Clock()
        # Create Scene Manager
        self.scene_manager = Scenes.SceneManager()
        # Is the Game running
        self.running = True

    # Load different Data like Sprites and Sounds
    def load_data(self):
        self.icon = pygame.image.load(Settings.Icon)
        pygame.mixer.music.load(Settings.StartMusic)

    # Generates an new Game
    # Must reset Variables and stuff
    def new(self):
        self.run()

    # The Whole Game
    # Does it need anything else?
    def run(self):
        # THE GAMELOOP
        while self.running:
            self.clock.tick(Settings.FPS)
            self.events()
            self.scene_manager.activeScene.handle_events(pygame.event.get(), self.scene_manager)
            self.scene_manager.activeScene.update()
            self.scene_manager.activeScene.render(self.screen)
        # Close the Game
        self.close()

    # The Events, like Key pressed and stuff
    def events(self):
        # What happens when you click the little X in the upper right corner
        if pygame.event.get(pygame.QUIT):
            self.running = False

    # Close The Game
    def close(self):
        # Shutdown Pygame and Sys
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.new()
