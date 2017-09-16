import configparser as c
import Settings
config = c.RawConfigParser()

def Read():
    config = c.RawConfigParser()
    config.read("Settings.cfg")
    Settings.ScreenWidth = config.getint("ScreenInfo", "ScreenWidth")
    Settings.ScreenHeight = config.getint("ScreenInfo", "ScreenHeight")
    Settings.Fullscreen = config.getboolean("ScreenInfo", "Fullscreen")
    Settings.FPS = config.getint("ScreenInfo", "FPS")
    Settings.Title = config.get("ScreenInfo", "Title")

    Settings.volume_music = config.getfloat("MusicInfo", "volume_music")
    Settings.volume_music_paused_screen = config.getfloat("MusicInfo", "volume_music_paused_screen")

def Write():
    config.add_section("ScreenInfo")
    config.set("ScreenInfo", "ScreenWidth", "Settings.ScreenWidth")
    config.set("ScreenInfo", "ScreenHeight", "Settings.ScreenHeight")
    config.set("ScreenInfo", "Fullscreen", "Settings.Fullscreen")
    config.set("ScreenInfo", "FPS", "Settings.FPS")

    config.add_section("MusicInfo")
    config.set("MusicInfo", "volume_music", "Settings.volume_music")
    config.set("MusicInfo", "volume_music_paused_screen", "Settings.volume_music_paused_screen")