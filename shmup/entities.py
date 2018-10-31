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
        self.image = self.__class__.Anim_Idle[self.frame]
        # Set transparecy
        self.image.set_colorkey((255, 255, 255))
        self.animation = 0
        self.frame = frame
        self.frame_count = 0
        self.animation_cycle = 1
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

    def update(self, dt, game_state):
        """
        Prcoedure updates the module and all appropriate AI/elements
        :param dt: time interval for
        :param game_state: GameScene or other wrapper for groups
        """
        # TODO collision detection to ensure does not move out of gamespace
        self.rect.move_ip(self.vy * dt, self.vx * dt)
        self.animate(dt)
        return

    def animate(self, dt=0):
        # TODO: Implement animation cycle. Google wiki for sources; would prefer static packaging instead of multi
        # TODO: step blitting, unless we overload Draw in our Groups [Which may be worthwhile]
        pass

    def fire(self, game_state):
        """
        Spawns Bullet in GameState
        :param game_state:
        :return:
        """
        # TODO make bullet class
        pass


class Bullet(pg.sprite):
    """
    Generic Bullet class
    Kills itself on Collision, as handled in main game loop, though may spawn other things like Explosion depending on
    collide code
    """

    def __init__(self, x, y, damage, image, speed, *groups):
        super(Bullet, self).__init__(groups)
        self.damage = damage
        self.image = image
        self.speed = speed
        self.rect = pg.Rect((x, y, x + 16, y + 16))  # TODO actual bullet size for collision

    def update(self, dt, game_state):
        """
        Moves the bullet up
        :param dt:
        :param game_state: Game state to modify
        :return:
        """
        self.rect.move_ip(0, self.speed * dt)
        return

    def colide(self, other):
        """
        Collision code for bullet
        :param other: Other Sprite that will have this script acting on it
        :return:
        """
        other.hp -= self.damage
        return


class Missile(Bullet):
    """
    Missile Class
    Extends Bullet but has group effect explossion
    """

    def __init__(self, x, y, image, speed, *groups):
        super(Missile, self).__init__(x, y, image, speed, *groups)
        pass
