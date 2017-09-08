import pygame, Color, Utilitys, Settings, Game

# Is the game paused
paused = False

class Scene(object):
    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events, scene_manager):
        raise NotImplementedError

class sceneManager(object):
    def __init__(self):
        self.go_to(TitleScene())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self

class TitleScene(Scene):
    def __init__(self):
        super(TitleScene, self).__init__()
        # Play a Sound
        pygame.mixer.music.play()

    def render(self, screen):
        # Resets the Screen
        screen.fill(Color.Black)
        # Write Some Text
        Utilitys.drawText("START",
                          128,
                          Color.White,
                          Settings.ScreenWidth / 2,
                          Settings.ScreenHeight / 8,
                          screen)
        Utilitys.drawText("Press Space to Continue...",
                          32,
                          Color.White,
                          Settings.ScreenWidth / 2,
                          Settings.ScreenHeight / 2,
                          screen)
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

    def render(self, screen):
        # Reset the screen to all black
        screen.fill(Color.Black)
        # Just for Testing
        Utilitys.drawText("GAME",
                          128,
                          Color.Green,
                          Settings.ScreenWidth / 2,
                          Settings.ScreenHeight / 8,
                          screen)

    def update(self):
        pass

    def handle_events(self, events, scene_manager):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                self.paused = True
                scene_manager.go_to(PauseScene())

class PauseScene(Scene):
    def __init__(self):
        super(PauseScene, self).__init__()
        # Set The Music Volume
        pygame.mixer.music.set_volume(Settings.volume_music_paused_screen)

    def render(self, screen):
        # Draw an transparent Background over everything else
        transparentBackground = pygame.Surface((Settings.ScreenWidth, Settings.ScreenHeight))
        transparentBackground.set_alpha(128)
        transparentBackground.fill(Color.Black)
        screen.blit(transparentBackground, (0, 0))
        # Write Some Text
        Utilitys.drawText("Pause",
                          64,
                          Color.Blue,
                          Settings.ScreenWidth / 2,
                          10,
                          screen)
        Utilitys.drawText("Press Space to Continue...", 32,
                          Color.Blue,
                          Settings.ScreenWidth / 2,
                          76,
                          screen)
        Utilitys.drawText("Press Escape to Quit", 32,
                          Color.Blue,
                          Settings.ScreenWidth / 2,
                          Settings.ScreenHeight - 32,
                          screen)

    def update(self):
        pass

    def handle_events(self, events, scene_manager):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                # Reset the Music Volume
                pygame.mixer.music.set_volume(Settings.volume_music)
                # End the pause
                paused = False
                scene_manager.go_to(GameScene())
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                scene_manager.go_to(EndScene())

class EndScene(Scene):
    def __init__(self):
        super(EndScene, self).__init__()

    def render(self, screen):
        screen.fill(Color.Black)
        # Write Some Text
        Utilitys.drawText("Thank you for playing!",
                          64,
                          Color.Red,
                          Settings.ScreenWidth / 2,
                          Settings.ScreenHeight / 4,
                          screen)
        Utilitys.drawText("press Escape to close",
                          32,
                          Color.Red,
                          Settings.ScreenWidth / 2,
                          Settings.ScreenHeight / 2,
                          screen)

    def update(self):
        pass

    def handle_events(self, events, scene_manager):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))


