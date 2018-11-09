import math
import random

import pygame as pg

import config


class TestEnemy(pg.sprite.Sprite):
    """
    Testing Entity
    """
    image = pg.image.load("../Assets/Wyrm.bmp")
    image = image.convert()
    image.set_colorkey(image.get_at((0, 0)))
    graphic_rect = pg.Rect(0, 0, 64, 64)
    collision_rect = pg.Rect(16, 0, 1664)
    def __init__(self, observer, x, y, *groups):
        self.x, self.y = x, y
        super().__init__(groups)
        self.observer = observer
        self.rect = __class__.graphic_rect.move(x, y)
        self.collide_rect = __class__.collision_rect.move(x, y)
        self.image = __class__.image
        self.hp = 30
        self.speed = 200
        self.vx, self.vy = 0, 0
        self.damage = 15
        self.shuffle_time = random.uniform(0, 2 * math.pi)
        # Colision Stuff
        self.has_collided = False
        self.collision_reset = 0

    def update(self, dt):
        # Check if Collision flag has been set
        # If it has, decrement the timer
        if self.collision_reset > 0:
            self.collision_reset -= dt
        if self.collision_reset <= 0:
            self.has_collided = False
        self.shuffle_time += dt
        if self.hp <= 0:
            self.observer.score(200)
            self.kill()
        if not config.GAME_RECT_EXTEND.contains(self.rect):
            self.kill()
        self.x += 75 * math.sin(5 * self.shuffle_time) * dt
        self.y += self.speed * dt
        self.rect = pg.Rect(self.x, self.y, 64, 64)
        self.collide_rect.x = self.x + 16
        # print(self.rect)
        return

    def collide(self, other, dt):
        if not self.has_collided:
            other.health -= self.damage
            self.has_collided = True
            self.collision_reset = 0.5
        else:
            pass
        return
