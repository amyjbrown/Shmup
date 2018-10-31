# Projectiles
# For Projectile Sprites and Logic
import pygame as pg


class Bullet(pg.sprite):
    """
    Generic Bullet class
    Kills itself on Collision, as handled in main game loop, though may spawn other things like Explosion depending on
    collide code
    """

    def __init__(self, x, y, damage, image, speed, observer, *groups):
        super(Bullet, self).__init__(groups)
        self.damage = damage
        self.observer = observer
        self.image = image
        self.speed = speed
        self.rect = pg.Rect((x, y, x + 16, y + 16))  # TODO actual bullet size for collision

    def update(self, dt):
        """
        Moves the bullet up
        :param dt:
        :return:
        """
        self.rect.move_ip(0, self.speed * dt)
        return

    def collide(self, other):
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
