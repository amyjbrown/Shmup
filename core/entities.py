# Entities and various ingame things
# Should use class methods for setup and image loading
import pygame as pg


# Actor class currently dead in the water but may be re-worked for Monster class
class Actor(pg.sprite.Sprite):
    """
    Actor Class
    To be overriden
    Class methods and variables useable as static
    Should include startup() for setting up sprite sheet, ala util.assetloader
    """

    def startup(cls):
        """
        Initializes all of the Static variables
        :return: None
        """
        pass

    def __init__(self, x, y, observer, *groups):
        super(Actor, self).__init__(*groups)
        self.x = x
        self.y = y
        self.observer = observer

        pass

    # Methods!

    def collide(self, other, dt):
        pass

    def on_death(self):
        pass

    def fire(self, *groups):
        pass

    def animate(self, dt):
        pass

