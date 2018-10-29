# Entites and various ingame things
# Should use class methods for setup and image loading
import pygame as pg


# Actor class currently dead in the water but may be re-worked for Monster class
class Actor(pg.sprite.Sprite):
    """
    Actor Class (Extends Sprite)
    Adds significant versaility for object interaction
    Contains Data  for efficient loading - sprite sheet stored in Class
    Methods overloaded or added
    act() Distinct AI function call
    update() Cleanup and "non-reactive" elements, e.g. dying, adding a life, score
    on_death() Internal cleanup and unique effects; e.g. explosion on death
    fire() None
    animate()
    """

    def __init__(self, x, y, frame=0, *groups):
        super(Actor, self).__init__(*groups)
        self.x = x
        self.y = y
        self.frame = frame
        """
        Creates new instance of Actor Class; to be overloaded
        :param x: X-position of top-left of sprite in Pygame coordinate system
        :param y: Y-position of top-left in pygame coordinate system
        :param frame: current animation frame
        :param groups:
        """
        pass

    # Methods!

    def act(self, *args):
        pass

    def collide(self, other):
        pass

    def on_death(self):
        pass

    def fire(self, *groups):
        pass

    def animate(self, dt):
        pass

    # Data should be read only and private - all variable elements should be in instance variables
    # Path for taking sprite info from
    Spritesheet = None
    # Graph_Rect: Use for size, and thus has form Rect(0,0,w,h)
    # Collision_Rect: Use for collision detection, and thus has form (x1,y1,x2,y2) where 0 =< x1 < x2 =< w \
    # and 0 =< y1 =< y2 =< h
    # List to contain normal animation images, of form (Image: Surface,time: Int)
    Anim_Idle = list()
    # List to contain dieing animation
    Anim_Die = list()
    # HP_Max Maximum life for an entity
    HP_Max = int()


class Player(pg.sprite.Sprite):
    Spritesheet = pg.image.load("../Assets/Ship.bmp")
    Graph_Rect = pg.Rect(0, 0, 64, 64)
    Anim_Idle = [Spritesheet]

    def __init__(self, x, y, lives=2, frame=0, hp=100, *groups):
        super(Player, self).__init__(groups)
        """
        :param x:
        :param y:
        :param lives:
        :param frame:
        :param groups
        """
        self.rect = pg.Rect(0, 0, 64, 64).move(x, y)
        # Starting health
        self.hp = hp
        # Class positions
        self.x = x
        self.y = y
        # Initial image and what to be blitted
        self.image = self.__class__.Anim_Idle[self.frame]
        # Set transparecy
        self.image.set_colorkey((255, 255, 255))
        # Flag for which animation state
        self.animation = 0
        # frame int to represent which integer of animation we're on
        self.frame = frame
        # Number of frames called currently, use for multiframe animation
        self.frame_count = 0
        self.animation_cycle = 1
        # Number of Respawns
        self.lives = lives
        self.speed = 2.5
        # Variables for "Direction" of movement; multiple by speed for update
        self.vx = 0
        self.vy = 0
        # cooldown - Frames between shots
        self.cooldown = 0
        return

    def set_direction(self, dx=None, dy=None):
        if dx is not None:
            self.vx = dx * self.speed
        if dy is not None:
            self.vy = dy * self.speed
        return

    def update(self, dt, *groups):
        """
        Prcoedure updates the module and all appropriate AI/elements
        :param dt: time interval for
        """
        self.x += self.vx * dt
        self.y += self.vy * dt
        # TODO collision detection to ensure does not move out of gamespace
        self.rect.move_ip(self.x, self.y)
        return

    def animate(self, dt=0):
        pass

    def fire(self, *groups):
        pass
