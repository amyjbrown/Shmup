#
# core game stuff
# Almost everything goes here
# Gonna be the heaviest boy
# TODO Decide whether or not procedure based input_parsing, or in main_loop
# TODO User movement inside of

import pygame as pg
import entities
import state
import screen





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
                self.game = False # Exit
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


    def run(self)->tuple:
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