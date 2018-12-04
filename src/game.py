# core core stuff
# Almost everything goes here
# TODO Decide whether or not procedure based input_parsing, or in main_loop
# TODO User movement inside of
# Changelog: Added GameState object into here
import pygame as pg

import config
import enemy
import player
import powerup
import projectile
import util


# GameScene Object
class GameScene:
    """
    Main GameScene object to hold primary core interactions
    Data that is held includes the various Sprite groups, metadata like score stuff
    """
    # Game Data
    PLAYER = player.Player
    ENEMY_DICT = {
        "test": enemy.TestEnemy
    }
    POWERUP = {
        "health": powerup.HealthToken
    }
    PROJECTILE = {
        "play bullet": projectile.Bullet,
    }

    def __init__(self, screen):
        """
        Creates new core scene
        """
        self.final: bool = False  # Use for quitting main game_loop
        self.next: str = None  # Use for setting next element
        self.next_params: dict = False
        # TODO - Config file for initializing Display, etc.

        self.screen = screen
        self.render_group = pg.sprite.Group()
        self.effects = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.tokens = pg.sprite.Group()
        self.ally_bullets = pg.sprite.Group()
        self.enemy_bullets = pg.sprite.Group()

        # Player Stuff
        self.player = player.Player(pg.Vector2(200, 200), self.render_group)
        self.lives = config.STARTING_LIVES

        # Score and combo stuff
        self.total_score = 0
        self.local_score = 0
        self.score_increment = config.LIFE_SCORE
        self.combo = int()
        self.combo_increment = int()
        self.combo_timer = float()
        self.combo_hits = config.COMBO_INCREMENTS
        self.combo_times = config.COMBO_TIME
        return

    def setup(self):
        """
        Performs pre-setup on all of the game objects
        :return: None
        """
        for element in self.ENEMY_DICT.values():
            element.setup()
        for element in self.POWERUP.values():
            element.setup()
        self.PLAYER.setup()
        pass

    def score(self, increment: int, combo: bool = False):
        """
        Adds increment to the score, optionally
        :param increment: Score increment
        :param combo: If true, increment combo, reset combo_timer
        :return: none
        """
        if combo:
            self.total_score += increment * self.combo
            self.local_score += increment * self.combo
            self.combo += 1
        else:
            self.total_score += increment
            self.local_score += increment

    def clear_level(self):
        """
        Clears all entities
        :return:
        """
        pass

    def load_level(self, level_id):
        """
        Loads and initializes the appropriate level
        :param level_id: Identifier of level to be loaded
        :return: None
        """
        pass

    def parse_input(self):
        """
        Parses and updates based on user_input
        :return: None
        """
        # input(list(events))
        # events = config.input_manager.get()
        events = config.input_manager.get()
        pressed = config.input_manager.pressed
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
                    enemy.TestEnemy(self, 200, -64, self.render_group, self.enemies)
                elif event.key == "debug2":
                    powerup.HealthToken(200, -64, self.render_group, self.tokens)
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
        """
        Updates game state by delta step
        :param dt: Time step for simulation
        :return: None
        """
        # Updates every entity, using delta time
        self.render_group.update(dt)
        # TODO spawns appropriate entities given Level_Time
        # Check for enemies colliding with player
        for sprite in pg.sprite.spritecollide(self.player, self.enemies, dokill=False):
            sprite.collide(self.player, dt)
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
        # Combo Shit
        # combo
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

    def spawn(self, **kwargs):
        pass
if __name__ == "__main__":
    pg.init()
    display = pg.display.set_mode((480, 640))
    game = GameScene(util.screen.Background(surface=display,
                                            im='C:/Users/Jonathan/PycharmProjects/shmup/Assets/BG1.bmp',
                                            r=pg.Rect(0, 0, 480, 640),
                                            speed=42))
    clock = pg.time.Clock()
    while not game.final:
        dt = clock.tick(60) / 1000
        events = config.input_manager.get()
        game.parse_input()
        game.update(dt)
        game.render(display)
        pg.display.set_caption("FPS: {:4.2f}, \t Score: {:.2f}\t Life: {:.2f}".
                               format((1 / dt), game.total_score, game.player.health))
