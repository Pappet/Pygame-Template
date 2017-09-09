import pygame
import Color
import Utilitys
import Settings
from Player import *

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
        self.go_to(TitleScene())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self


class TitleScene(Scene):
    def __init__(self):
        super(TitleScene, self).__init__()

    def render(self, screen):
        # Resets the Screen
        screen.fill(Color.Black)
        # Write Some Text
        Utilitys.draw_text("START", 128, Color.White, Settings.ScreenWidth / 2, Settings.ScreenHeight / 8, screen)
        Utilitys.draw_text("Press Space to Continue...", 32, Color.White, Settings.ScreenWidth / 2,
                           Settings.ScreenHeight / 2, screen)
        pygame.display.flip()

    def update(self):
        pass

    def handle_events(self, events, scene_manager):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                scene_manager.go_to(GameScene())


class GameScene(Scene):
    def __init__(self):
        super(GameScene, self).__init__()
        # Play a Sound
        pygame.mixer.music.play()
        self.paused = False
        # Group for all Sprites
        # Do i need this???
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)

    def render(self, screen):
        if not self.paused:
            # Reset the screen to all black
            screen.fill(Color.Black)
            # Just for Testing
            Utilitys.draw_text("GAME", 128, Color.Green, Settings.ScreenWidth / 2, Settings.ScreenHeight / 8, screen)
            self.all_sprites.draw(screen)
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
                        scene_manager.go_to(EndScene())
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
