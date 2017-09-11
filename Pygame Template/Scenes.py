from Player import *
import pygame
import Utilitys
import GUI
import Color
import Settings


class Scene(object):
    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events, scene_manager):
        raise NotImplementedError


class SceneManager(object):
    def __init__(self):
        self.titleScene = TitleScene()
        self.optionsScene = OptionsScene()
        self.gameScene = GameScene()
        self.endScene = EndScene()

        self.activeScene = self.titleScene

        self.go_to(self.activeScene)

    def go_to(self, scene):
        if scene == "TitleScene":
            self.activeScene = self.titleScene
        if scene == "OptionsScene":
            self.activeScene = self.optionsScene
        if scene == "GameScene":
            self.activeScene = self.gameScene
        if scene == "EndScene":
            self.activeScene = self.endScene
        self.activeScene.manager = self


class TitleScene(Scene):
    def __init__(self):
        super(TitleScene, self).__init__()
        # Menu Buttons
        self.playButton = GUI.Button("Play", 75, 250, Settings.ScreenHeight - 350)
        self.optionsButton = GUI.Button("Options", 75, 250, Settings.ScreenHeight - 200)
        self.exitButton = GUI.Button("Exit", 75, 250, Settings.ScreenHeight - 50)
        # Group all Buttons
        self.allButtons = (self.playButton, self.optionsButton, self.exitButton)
        print("New Title")

    def render(self, screen):
        # Resets the Screen
        screen.fill(Color.Blue)
        # V - Here is stuff drawn

        for a in self.allButtons:
            a.draw(screen)

        # A - Here is stuff drawn
        pygame.display.flip()

    def update(self):
        for a in self.allButtons:
            a.update()

    def handle_events(self, events, scene_manager):
        if "clicked" in self.playButton.handle_events():
            scene_manager.go_to("GameScene")
        if "clicked" in self.optionsButton.handle_events():
            scene_manager.go_to("OptionsScene")
        if "clicked" in self.exitButton.handle_events():
            scene_manager.go_to("EndScene")

        for a in self.allButtons:
            a.handle_events()

class OptionsScene(Scene):
    def __init__(self):
        super(OptionsScene, self).__init__()
        self.backButton = GUI.Button("Back", 75, 250, Settings.ScreenHeight - 50)
        # Group all Buttons
        self.allButtons = (self.backButton)

    def render(self, screen):
        # Resets the Screen
        screen.fill(Color.Blue)
        # V - Here is stuff drawn
        self.backButton.draw(screen)
        # A - Here is stuff drawn
        pygame.display.flip()

    def update(self):
        pass

    def handle_events(self, events, scene_manager):
        if "clicked" in self.backButton.handle_events():
            scene_manager.go_to("TitleScene")


class GameScene(Scene):
    def __init__(self):
        super(GameScene, self).__init__()
        # Play a Sound
        pygame.mixer.music.play()
        self.paused = False
        # Group for all Sprites
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)

    def render(self, screen):
        if not self.paused:
            # Reset the screen to all black
            screen.fill(Color.Black)
            # V - Here is stuff drawn

            self.all_sprites.draw(screen)

            # A - Here is stuff drawn
        else:
            # Draw an transparent Background over everything else
            transparent_background = pygame.Surface((Settings.ScreenWidth, Settings.ScreenHeight))
            transparent_background.set_alpha(5)
            transparent_background.fill(Color.Black)
            screen.blit(transparent_background, (0, 0))
            # Write Some Text
            Utilitys.draw_text("Pause", 64, Color.Blue, Settings.ScreenWidth / 2, 10, screen)
            Utilitys.draw_text("Press Space to Continue...", 32, Color.Blue,
                               Settings.ScreenWidth / 2, 76, screen)
            Utilitys.draw_text("Press Escape to Quit", 32, Color.Blue,
                               Settings.ScreenWidth / 2, Settings.ScreenHeight - 32, screen)
        pygame.display.flip()

    def update(self):
        if not self.paused:
            self.all_sprites.update()
        else:
            pass

    def handle_events(self, events, scene_manager):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    if not self.paused:
                        self.paused = True
                        # Set The Music Volume
                        pygame.mixer.music.set_volume(Settings.volume_music_paused_screen)
                    else:
                        scene_manager.go_to("EndScene")
                if e.key == pygame.K_SPACE:
                    self.paused = False
                    # Reset the Music Volume
                    pygame.mixer.music.set_volume(Settings.volume_music)


class EndScene(Scene):
    def __init__(self):
        super(EndScene, self).__init__()
        # Stops the Music
        pygame.mixer.music.fadeout(500)

    def render(self, screen):
        screen.fill(Color.Black)
        # V - Here is stuff drawn

        # Write Some Text
        Utilitys.draw_text("Thank you for playing!", 64, Color.Red,
                           Settings.ScreenWidth / 2, Settings.ScreenHeight / 4, screen)
        Utilitys.draw_text("press Escape to close", 32, Color.Red,
                           Settings.ScreenWidth / 2, Settings.ScreenHeight / 2, screen)

        # A - Here is stuff drawn
        pygame.display.flip()

    def update(self):
        pass

    def handle_events(self, events, scene_manager):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))


class DefaultScene(Scene):
    def __init__(self):
        super(DefaultScene, self).__init__()

    def render(self, screen):
        pass

    def update(self):
        pass

    def handle_events(self, events, scene_manager):
        pass
