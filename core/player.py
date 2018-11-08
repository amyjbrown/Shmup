# Player class
import pygame as pg

import config
import projectile


class Player(pg.sprite.Sprite):
    Spritesheet = pg.image.load("../Assets/Ship.bmp")
    Spritesheet.convert()
    Graph_Rect = pg.Rect(0, 0, 64, 64)
    Anim_Idle = [Spritesheet]

    def __init__(self, x, y, observer, *groups):
        super(Player, self).__init__(groups)
        """
        :param x:
        :param y:
        :param observer
        :param *groups
        """
        # Observer entity for monitoring and handling actor
        self.observer = observer
        self.rect = pg.Rect(0, 0, 64, 64).move(x, y)
        # Starting health
        self.health = 100
        # Load Image and setup
        self.frame = 0
        self.image = self.__class__.Anim_Idle[0]
        self.image.set_colorkey((255, 255, 255))
        self.image.convert()
        # Enum for animation
        self.animation = 0
        self.frame = 0
        self.frame_count = 0
        # Length of animation cycle
        self.animation_cycle = 1
        self.speed = 120  # Pixels/Second
        # Variables for "Direction" of movement; multiple by speed for update
        self.vx = 0
        self.vy = 0
        # cooldown - Frames between shots
        self.cooldown = 0
        self.COOLDOWN_MAX = 1 / 10
        # Fire side - used for alternating fire
        self.fire_side = False
        return

    def update(self, dt):
        """
        Prcoedure updates the module and all appropriate AI/elements
        :param dt: time interval for
        """
        # TODO collision detection to ensure does not move out of gamespace
        if config.GAME_RECT.contains(self.rect.move(0, self.vy * dt)):
            self.rect.move_ip(0, self.vy * dt)
        if config.GAME_RECT.contains(self.rect.move(self.vx * dt, 0)):
            self.rect.move_ip(self.vx * dt, 0)
        self.cooldown -= dt
        # self.animate(dt)
        return

    def notify(self, entity, event):
        """
        MUT Sends notification method to observer
        """
        self.observer.on_notify(entity, event)
        pass

    def animate(self, dt=0):
        # TODO: Implement animation cycle. Google wiki for sources; would prefer static packaging instead of multi
        # TODO: step blitting, unless we overload Draw in our Groups [Which may be worthwhile]
        pass

    def fire(self):
        """
        Sends Spawn Bullet to Observer
        :return:
        """
        if self.cooldown <= 0:
            projectile.Bullet(self.observer,
                              self.rect.x + 20 + 8 * self.fire_side,
                              self.rect.y - 5,
                              self.observer.render_group, self.observer.ally_bullets)
            self.cooldown = self.COOLDOWN_MAX
            self.fire_side = not self.fire_side
        return
