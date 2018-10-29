#
# core game stuff
# Almost everything goes here
# Gonna be the heaviest boy
# TODO Decide whether or not procedure based input_parsing, or in main_loop
# TODO User movement inside of
# Changelog: Added GameState object into here
import pygame as pg

import entities
import scene
import screen


class GameState:
    """
    Container object for everything you need in the main game.
    Use this to pass around data to scenes or for initialization
    """

    def __init__(self, ):
        pass


# GameScene Object
class GameScene(scene.Scene):
    """
    Main GameScene object to hold primary game interactions
    Data that is held includes the various Sprite groups, metadata like score stuff
    """

    def __init__(self, state: GameState = None, **settings):
        """
        Creates new game scene with optional GameState
        :param state: Previous GameState to be loaded in, if None state is initialized
        """
        self.final: bool = False  # Use for quitting main game_loop
        self.next: str = None  # Use for setting next element
        self.next_params: dict = False
        if state is None:
            # Player Initialization
            # TODO move a lot of info out of player
            self.player = entities.Player(200, 200)
            # Groups
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
        else:
            return  # Do GameState Unwrapping

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
                    self.player.fire(self.ally_bullets)
                # TODO other specials
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
        self.render_group.update(dt)
        # TODO spawns appropriate entities given Level_Time
        # Check for enemies colliding with player
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
        # TODO how to check for score
        # TODO logic on player if player is alive
        # TODO Screen object should be scrolled by dt
        return

    def render(self, screen):
        """

        :param screen: screen.Screen object to utilize
        :return:
        """
        # blit background
        # Blit main
        self.render_group.draw(screen.play_screen)
        pass


### Delete This but scavenge what you can
class PlayState(state.State):
    def __init__(self, mainscreen):
        """
        Does level loading and settup
        :param level:
        :param player: Player-info
        """
        # Draw Prolog + Begining Background
        # Wait for full loading/init
        # Then START BOI
        #
        self.screen = mainscreen
        self.playscreen = screen.Background(mainscreen,
                                            im='../Assets/BG1.bmp',
                                            r=pg.Rect(0, 0, 400, 640))
        # Set up main Clock mechanism
        self.clock = pg.time.Clock()
        # Set up groups
        self.render_group = pg.sprite.Group()
        self.player_group = pg.sprite.GroupSingle()
        # TODO Implement non-bespoke background rendering
        self.player = entities.Player(200, 400, 2, 0, 100, self.render_group, self.player_group)
        #
        self.game = True

    def input(self):
        """
        Procedure to update various information
        :return:
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game = False  # Exit
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    self.player.set_direction(dy=1)
                elif event.key == pg.K_UP:
                    self.player.set_direction(dy=-1)
                elif event.key == pg.K_RIGHT:
                    self.player.set_direction(dx=1)
                elif event.key == pg.K_LEFT:
                    self.player.set_direction(dx=-1)
                elif event.key == pg.K_ESCAPE:
                    self.player.speed = float(input("Enter new player speed: "))
            elif event.type == pg.KEYUP:
                if event.key == pg.K_DOWN:
                    self.player.set_direction(dy=0)
                elif event.key == pg.K_UP:
                    self.player.set_direction(dy=0)
                elif event.key == pg.K_RIGHT:
                    self.player.set_direction(dx=0)
                elif event.key == pg.K_LEFT:
                    self.player.set_direction(dx=0)
        return

    def run(self) -> tuple:

        """
        Procedure Main gameplay. All game actions occur in here
        Level selection and player params set by __init__
        :return: Playgame, Params | Menu | Quit
        """

        # Main Game Loop
        while self.game:
            dt = self.clock.tick(60)
            self.input()
            # Manage Input, to be place into a subroutine soon
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    play_game = False
                # Now for all of the player input shit
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        play_game = False
            # Do Game Logic Updates!
            self.player.update()
            # Background scrolling and rendering
            self.playscreen.scroll()
            # Draw all objects onto it's screen
            self.render_group.draw(self.playscreen.surface)
            pg.display.flip()

        print("Fuck Yeah!")
        return "play", dict()


# Main Testing!
if __name__ == "__main__":
    pg.init()
    display = pg.display.set_mode((400, 640))
    play = PlayState(display)
    play.run()
