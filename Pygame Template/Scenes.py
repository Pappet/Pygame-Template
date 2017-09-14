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
<<<<<<< HEAD
        self.activeScene = TitleScene()
        self.go_to(self.activeScene)

    def go_to(self, scene):
        self.activeScene = scene
        self.activeScene.manager = self
=======
        self.go_to(TitleScene())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self
>>>>>>> parent of 2223a89... Rewriten Scene handling

    def new_scene(self, scene):
        self.activeScene = scene()


class TitleScene(Scene):
    def __init__(self):
        super(TitleScene, self).__init__()

        self.playButton = GUI.Button("Play", 75, Settings.ScreenWidth / 2, Settings.ScreenHeight / 6)
        self.optionsButton = GUI.Button("Options", 75, Settings.ScreenWidth / 2, Settings.ScreenHeight / 3)
        self.exitButton = GUI.Button("Exit", 75, Settings.ScreenWidth / 2, Settings.ScreenHeight / 2)

        self.allButtons = (self.playButton, self.optionsButton, self.exitButton)

    def render(self, screen):
        # Resets the Screen
        screen.fill(Color.Blue)

        for a in self.allButtons:
            a.draw(screen)

        pygame.display.flip()

    def update(self):
        for a in self.allButtons:
            a.update()

    def handle_events(self, events, scene_manager):
        if "clicked" in self.playButton.handle_events():
<<<<<<< HEAD
            scene_manager.new_scene("GameScene")
        if "clicked" in self.optionsButton.handle_events():
            scene_manager.go_to("OptionsScene")
        if "clicked" in self.exitButton.handle_events():
            scene_manager.new_scene("EndScene")
=======
            print("clicked")
            scene_manager.go_to(GameScene())
        if "" in self.optionsButton.handle_events():
            pass
        if "clicked" in self.exitButton.handle_events():
            scene_manager.go_to(EndScene())
>>>>>>> parent of 2223a89... Rewriten Scene handling

        for a in self.allButtons:
            a.handle_events()


class GameScene(Scene):
    def __init__(self):
        super(GameScene, self).__init__()
        # Play a Sound
        pygame.mixer.music.play()
        self.paused = False

        self.titles = ("Map", "Inventory", "Quests", "Menu", "pups", "Astrid")
        self.buttons = GUI.ButtonGrid(self.titles, 75, "Bottom")

        # Group for all Sprites
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)

    def render(self, screen):
        if not self.paused:
            # Reset the screen to all black
            screen.fill(Color.Black)
            # Just for Testing
            #Utilitys.draw_text("GAME", 128, Color.Green, Settings.ScreenWidth / 2, Settings.ScreenHeight / 8, screen)
            self.all_sprites.draw(screen)
            for b in self.buttons:
                b.draw(screen)
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
            for b in self.buttons:
                b.update()
        else:
            pass

    def handle_events(self, events, scene_manager):
        for b in self.buttons:
            b.handle_events()

        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    if not self.paused:
                        self.paused = True
                        # Set The Music Volume
                        pygame.mixer.music.set_volume(Settings.volume_music_paused_screen)
                    else:
<<<<<<< HEAD
                        scene_manager.new_scene("EndScene")
=======
                        scene_manager.go_to(EndScene())
>>>>>>> parent of 2223a89... Rewriten Scene handling
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
        # Write Some Text
        Utilitys.draw_text("Thank you for playing!", 64, Color.Red,
                           Settings.ScreenWidth / 2, Settings.ScreenHeight / 4, screen)
        Utilitys.draw_text("press Escape to close", 32, Color.Red,
                           Settings.ScreenWidth / 2, Settings.ScreenHeight / 2, screen)
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
