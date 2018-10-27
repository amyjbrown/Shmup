import json
import pygame
# General class Structure
# Code notes:
# Procedure - explicit side effects outside of parameters, may or may not have return value
# Semi-pure/Mutator - "semi-pure" - may induce side effects in parameters, may or may not have return value
# Pure - has explicit return value and no side effects
# Data based approach - Dynamic class creation
# create_entities -> List[Entities];
# Entities = type(json.name, json.(hierachy objects), json.dict
import pygame
sprite = pygame.sprite
Rect = pygame.Rect
import typing


class Actor(sprite.Sprite):
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
    def __init__(self,x,y,frame = 0, *groups):
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

    def fire(self):
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


class ActorGroup(sprite.Group):
    """
    Actor Group Class

    Extends Group by adding an additional interface element, act()
    Actor objects have two distinct elements, act() and update()
    """
    def act(self, *args):
        """Mutator Call the act method of every member sprite
        any return values from sprite.act() cannot be retrieved
        :arg args to be passed
        :return None
        """
        for s in self.sprites():
            s.act(*args)

# Implementation of usable Player stuff


class Player(Actor):
    Spritesheet = pygame.image.load("../Assets/Ship.bmp")
    Graph_Rect = Rect(0, 0, 64, 64)
    Anim_Idle = [Spritesheet]

    def __init__(self, x, y, lives=2, frame=0, hp=100, *groups):
        super(Player, self).__init__(x, y, frame, groups)
        """
        :param x:
        :param y:
        :param lives:
        :param frame:
        :param groups
        """
        self.rect = Rect(0, 0, 64, 64).move(x, y)
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
            self.vx = dx* self.speed
        if dy is not None:
            self.vy = dy * self.speed
        return

    def update(self, *args):
        """
        Prcoedure updates the module and all appropriate AI/elements
        :param args: todo implement this bullshit
        """
        self.x += self.vx
        self.y += self.vy
        self.rect.move_ip(self.vx * self.speed, self.vy * self.speed)
        # print(str(self.x) + " " + str(self.y))
        return

    def animate(self, dt=0):
        pass