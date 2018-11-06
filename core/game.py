# core core stuff
# Almost everything goes here
# Gonna be the heaviest boy
# TODO Decide whether or not procedure based input_parsing, or in main_loop
# TODO User movement inside of
# Changelog: Added GameState object into here
import random

import pygame as pg

import config
import enemy
import player
import powerup
import util.screen


# GameScene Object
class GameScene:
    """
    Main GameScene object to hold primary core interactions
    Data that is held includes the various Sprite groups, metadata like score stuff
    """

    def __init__(self, screen):
        """
        Creates new core scene with optional GameState
        """
        self.final: bool = False  # Use for quitting main game_loop
        self.next: str = None  # Use for setting next element
        self.next_params: dict = False
        # Player Initialization
        # Groups
        # self.player_screen = screen.Background() Init details
        # TODO - Config file for initializing Display, etc.
        self.screen = screen
        self.render_group = pg.sprite.Group()
        self.effects = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.tokens = pg.sprite.Group()
        self.ally_bullets = pg.sprite.Group()
        self.enemy_bullets = pg.sprite.Group()
        # Player Stuff
        self.player = player.Player(200, 200, self, self.render_group)
        self.lives = 2
        self.total_score = 0
        self.local_score = 0
        self.score_increment = 5000
        return

    def score(self, increment):
        self.total_score += increment
        self.local_score += increment

    def reset(self):
        """
        MUT resets the GameScene so all state information is null, all groups empty etc.
        :return: None
        """
        pass

    def parse_input(self, pressed, events):
        """
        Parses and updates based on user_input
        :param pressed:
        :param events: Events to be parsed through
        :return: None
        """
        # input(list(events))
        # events = config.input_manager.get()
        for event in events:
            if event.key == "QUIT":
                self.final = True  # Quit loop
            elif event.down:
                if event.key == "menu":
                    # TODO params for pause menu
                    pass
                    # self.next = "MENU"
                elif event.key == "missile":
                    pass
                elif event.key == "bomb":
                    print("Bomba")
                elif event.key == "debug1":
                    enemy.TestEnemy(self, random.randrange(0, 363), -64, self.render_group, self.enemies)
                elif event.key == "debug2":
                    powerup.HealthToken(self, random.randrange(0, 363), -64, self.render_group, self.tokens)
                elif event.key == "debug3":
                    print("got3")
                elif event.key == "debug4":
                    print("Got4")


        # Now for smoother movement
        # Ensures no pausing
        if pressed["left"] and not pressed["right"]:
            self.player.vx = -self.player.speed
        elif pressed["right"] and not pressed["left"]:
            self.player.vx = +self.player.speed
        else:
            self.player.vx = 0

        # Vertical movement
        if pressed["up"] and not pressed["down"]:
            self.player.vy = -self.player.speed
        elif pressed["down"] and not pressed["up"]:
            self.player.vy = +self.player.speed
        else:
            self.player.vy = 0
        # Do rest
        if pressed["fire"]:
            self.player.fire()
        return

    def update(self, dt):
        # Updates every entity, using delta time
        self.render_group.update(dt)
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
            token.collide(self.player)
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
        self.render_group.draw(self.screen.surface)
        pg.display.update(self.screen.rect)
        pass


if __name__ == "__main__":
    pg.init()
    display = pg.display.set_mode((400, 640))
    game = GameScene(util.screen.Background(surface=display,
                                            im='C:/Users/Jonathan/PycharmProjects/shmup/Assets/BG1.bmp',
                                            r=pg.Rect(0, 0, 400, 640),
                                            speed=42))
    clock = pg.time.Clock()
    while not game.final:
        dt = clock.tick(60) / 1000
        events = config.input_manager.get()
        game.parse_input(config.input_manager.pressed, events)
        game.update(dt)
        game.render(display)
        pg.display.set_caption("FPS: {:4.2f}, \t Score: {}".format((1 / dt), game.total_score))
