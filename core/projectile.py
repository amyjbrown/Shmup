# Projectiles
# For Projectile Sprites and Logic
import pygame as pg

import config


class Bullet(pg.sprite.Sprite):
    """
    Generic Bullet class
    Kills itself on Collision, as handled in main core loop, though may spawn other things like Explosion depending on
    collide code
    """
    image = pg.image.load("../Assets/player bullet.bmp")
    image.set_colorkey(image.get_at((0, 0)))

    def __init__(self, observer, x, y, *groups):
        super(Bullet, self).__init__(groups)
        self.damage = 10  # Defaults
        self.observer = observer
        self.speed = 300
        self.rect = pg.Rect(0, 0, 16, 16).move(x, y)  # TODO actual bullet size for collision
        self.image = self.__class__.image
        # Load image

    def update(self, dt):
        """
        Moves the bullet up
        :param dt:
        :return:
        """
        self.rect.move_ip(0, -self.speed * dt)
        if not config.GAME_RECT.contains(self.rect):
            self.kill()
        return

    def collide(self, other):
        """
        Collision code for bullet
        :param other: Other Sprite that will have this script acting on it
        :return: None
        """
        other.hp -= self.damage
        self.kill()
        return



