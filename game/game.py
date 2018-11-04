# core game stuff
# Almost everything goes here
# Gonna be the heaviest boy
# TODO Decide whether or not procedure based input_parsing, or in main_loop
# TODO User movement inside of
# Changelog: Added GameState object into here
import pygame as pg

import util
from . import player


# GameScene Object
class GameScene:
    """
    Main GameScene object to hold primary game interactions
    Data that is held includes the various Sprite groups, metadata like score stuff
    """

    def __init__(self, screen):
        """
        Creates new game scene with optional GameState
        """
        self.final: bool = False  # Use for quitting main game_loop
        self.next: str = None  # Use for setting next element
        self.next_params: dict = False
        # Player Initialization
        # Groups
        # self.player_screen = screen.Background() Init details
        # TODO - Config file for initializing Display, etc.
        self.screen = screen
        self.player = player.Player(200, 200, self, self.render_group)
        self.render_group = pg.sprite.Group()
        self.effects = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.tokens = pg.sprite.Group()
        self.ally_bullets = pg.sprite.Group()
        self.enemy_bullets = pg.sprite.Group()
        self.lives = 2
        self.total_score = 0
        self.local_score = 0
        self.score_increment = 5000
        return

    def reset(self):
        """
        MUT resets the GameScene so all state information is null, all groups empty etc.
        :return: None
        """
        pass

    def parse_input(self, *events):
        """
        Takes in
        :param events: Events to be parsed
        :return:
        """
        for event in events:
            if event.key == "QUIT":
                self.final = True  # Quit loop
            elif event.down:
                if event.key == "up":
                    self.player.vy = -self.player.speed
                elif event.key == "down":
                    self.player.vy = self.player
                elif event.key == "left":
                    self.player.vx = -self.player.speed
                elif event.key == "right":
                    self.player.vx = self.player.speed
                elif event.key == "menu":
                    # TODO params for pause menu
                    self.next = "MENU"
                elif event.key == "space":
                    self.player.fire()
                elif event.key == "missile":
                    pass
                elif event.key == "bomb":
                    pass
                # TODO other specials
            # Set the movement to zero if Key_
            elif event.up:
                if event.key == "up":
                    self.player.vy = 0
                elif event.key == "down":
                    self.player.vy = 0
                elif event.key == "left":
                    self.player.vx = 0
                elif event.key == "right":
                    self.player.vx = 0
        pass

    def update(self, dt):
        # Updates every entity, using delta time
        self.render_group.update(dt, self)
        # TODO spawns appropriate entities given Level_Time
        # Check for enemies colliding with player
        # TODO for peformance switch to less performance heavy lis parsing
        for sprite in pg.sprite.spritecollide(self.player, self.enemies, dokill=False):
            sprite.collide(self.player)
        # Check for bullets
        for bullet in pg.sprite.spritecollide(self.player, self.enemy_bullets, dokill=True):
            bullet.collide(self.player)
        # do group_collide with friendly bullets and enemies
        for token in pg.sprite.spritecollide(self.player, self.tokens, dokill=True):
            token.effect(self.player)
        # Checks collision between friendly bullets and enemies bullets, apply bullet effects to each
        collide_dict = pg.sprite.groupcollide(self.enemies, self.ally_bullets, dokilla=False, dokillb=True)
        for enemy in collide_dict:
            for bullet in collide_dict[enemy]:
                bullet.collide(enemy)
        # DONE:= Score will be increased via enemies that die during their update methods
        # TODO logic on player if player is alive
        self.screen.scroll(dt)
        return

    def render(self, display):
        """
        PROC Screen may be removed in future versions
        :return:
        """
        self.render_group.draw(self.screen)
        pg.display.update(self.screen.rect)
        pass


if __name__ == "__main__":
    display = pg.display.set_mode((400, 640))
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
    game = GameScene(util.screen.Background(surface=display,
                                            im='C:/Users/Jonathan/PycharmProjects/shmup/Assets/BG1.bmp',
                                            r=pg.Rect(0, 0, 400, 640),
                                            speed=42))
    clock = pg.time.Clock()
    while not game.final:
        dt = clock.Tick(60) / 1000
        game.parse_input(input_manager.get())
        game.update(dt)
        game.render(display)
