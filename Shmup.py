# Main Boi
# Finally done for sense of scale
# Imports
import pygame as pg

import shmup

# Initialize PyGame Display and custom scene
display = pg.display.set_mode((480, 640))

# Setup event_manager and data
keys = ["up", "down", "left", "right", "fire", "missile", "bomb", "menu"]
key_map = {"up": [pg.K_UP, pg.K_w],
           "down": [pg.K_DOWN, pg.K_s],
           "right": [pg.K_RIGHT, pg.K_d],
           "left": [pg.K_LEFT, pg.K_a],
           "menu": [pg.K_ESCAPE],
           "fire": [pg.K_SPACE],
           "missile": [pg.K_x],
           "bomb": [pg.K_z],
           }
event_manager = shmup.myevent.EventManager(keys, key_map)
# Sound Manager - Still to do
sound_manager = 0
# Scene manager set up
states = {
    "game": shmup.game.GameScene,
}
manager = shmup.scene.SceneManager(states, "game")
# Do Main Game Loop!
manager.main_loop()
# Once done, system exit
quit()
