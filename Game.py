import pygame, sys, random, Color, Utilitys
from Settings import *

class Game:
    #Initiales The Game
    def __init__(self):
        #Initiales Pygame and the Sound Mixer
        pygame.init()
        pygame.mixer.init()
        #Generate a Screen to Display stuff
        self.screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
        #Set the Window Name
        pygame.display.set_caption(ScreenTitle)
        #Load a Font
        self.font = pygame.font.match_font(FONT)
        #Initiales the Clock to limit the Gamespeed
        self.clock = pygame.time.Clock()
        #Is the Game running
        self.running = True
        #Is the game paused
        self.paused = False
        #Groupe for all Sprites
        #Do i need this here???
        self.all_sprites = pygame.sprite.Group()

    #Generates an new Game
    #Must reset Variables and stuff
    def new(self):
        self.run()

    #The Whole Game
    #Does it need anything else?
    def run(self):
        #Show the Start Screen
        self.StartScreen()
        #THE GAMELOOP
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.render()
        #Show something when the Game is closing
        self.EndScreen()
        #Close the Game
        self.close()

    #The Events, like Key pressed and stuff
    def events(self):
        #Get all Events
        for event in pygame.event.get():
            #What happens when you click the little X in the upper right corner
            if event.type == pygame.QUIT:
                self.running = False
                break
            if event.type == pygame.KEYDOWN:
                #What happens when you click the Escape Key
                if event.key == pygame.K_ESCAPE:
                    # Pause the Game
                    self.paused = True

    #Here comes the Gamemechanics
    def update(self):
        if not self.paused:
            pass
        else:
            pass

    #Rendering the Stuff on the Screen
    def render(self):
        #Check if the Game is paused
        if not self.paused:
            #if not render the normal Game stuff
            #Reset the screen to all black
            self.screen.fill(Color.Black)
            #Just for Testing
            Utilitys.drawText("GAME", 128, Color.Green, ScreenWidth / 2, ScreenHeight / 2, self.screen)
        else:
            #if its paused render the Pause Screen
            self.PauseScreen()
        #needed for double Buffering
        pygame.display.flip()

    # Close The Game
    def close(self):
        #Shutdown Pygame and Sys
        pygame.quit()
        sys.exit()

    # Basic Start Screen with Text Infos
    def StartScreen(self):
        self.screen.fill(Color.Black)
        Utilitys.drawText("START",128,Color.White,ScreenWidth/2, ScreenHeight/2,self.screen)
        pygame.display.flip()
        #Waiting until Player presses a Key to Continue
        Utilitys.wait_for_key(self, self.paused)

    # Basic End Screen with Text Infos
    def EndScreen(self):
        self.screen.fill(Color.Black)
        Utilitys.drawText("End", 128, Color.Red, ScreenWidth / 2, ScreenHeight / 2, self.screen)
        pygame.display.flip()

    # Basic Pause Screen with Text Infos
    def PauseScreen(self):
        # Draw an transparent Background over everything else
        transparentBackground = pygame.Surface((ScreenWidth,ScreenHeight))
        transparentBackground.set_alpha(128)
        transparentBackground.fill(Color.Black)
        self.screen.blit(transparentBackground,(0,0))
        #Write Some Text
        Utilitys.drawText("Pause", 64, Color.RandomColor(), ScreenWidth / 2, 10, self.screen)
        Utilitys.drawText("Press any Key to Continue...", 32, Color.RandomColor(), ScreenWidth / 2, 76, self.screen)
        Utilitys.drawText("Press Escape to Quit", 32, Color.RandomColor(), ScreenWidth / 2, ScreenHeight - 32, self.screen)
        pygame.display.flip()
        # Waiting until Player presses a Key to Continue
        Utilitys.wait_for_key(self, self.paused)
        # End the pause
        self.paused = False
