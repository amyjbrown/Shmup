import pygame as pg

import util

# Define prebakes
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

input_manager = util.input.EventManager(keys, key_map)
sound_manager = None
