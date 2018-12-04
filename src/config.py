import pygame as pg

import util

# Game Area
GAME_AREA = [480, 640]  # TODO change all assets over to 480x640
GAME_RECT = pg.Rect(0, 0, 480, 640)
GAME_RECT_EXTEND = pg.Rect(-64, -64, 608, 768)
__author__ = "Amy Brown"
# Define prebakes

KEYS = ["up", "down", "left", "right", "fire", "missile", "bomb", "menu",
        "debug1", "debug2", "debug3", "debug4", "debug5"]
KEY_MAP = {"up": [pg.K_UP, pg.K_w],
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
# SCORE AND COMBO DETAILS
LIFE_SCORE = 15000
COMBO_INCREMENTS = [3, 5, 10, 15]  # For combo X1 -> X2, X2 -> X3, X3 -> X4, X4 -> X5
COMBO_TIME = [10.0, 10.0, 8.0, 5.0, 3.0]  # For Combo times of X1, X2, X3, X4, X5
STARTING_LIVES = 2

input_manager = util.input.EventManager(KEYS, KEY_MAP)
