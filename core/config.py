import pygame as pg

import util.input

# Game Area
GAME_AREA = [400, 640]  # TODO change all assets over to 480x640
GAME_RECT = pg.Rect(0, 0, 400, 640)
GAME_RECT_EXTEND = pg.Rect((-64, -64,), (464, 704))
__author__ = "Amy Brown <3"
DISPLAY = pg.display.set_mode(GAME_AREA)
# Define prebakes

keys = ["up", "down", "left", "right", "fire", "missile", "bomb", "menu",
        "debug1", "debug2", "debug3", "debug4", "debug5"]

key_map = {"up": [pg.K_UP, pg.K_w],
           "down": [pg.K_DOWN, pg.K_s],
           "right": [pg.K_RIGHT, pg.K_d],
           "left": [pg.K_LEFT, pg.K_a],
           "menu": [pg.K_ESCAPE],
           "fire": [pg.K_SPACE],
           "missile": [pg.K_x],
           "bomb": [pg.K_z],
           "debug1": [pg.K_1],
           "debug2": [pg.K_2],
           "debug3": [pg.K_3],
           "debug4": [pg.K_4],
           "debug5": [pg.K_5]
           }

input_manager = util.input.EventManager(keys, key_map)
sound_manager = None
