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

    def __init__(self, observer, x, y, *groups):
        self.x, self.y = x, y
        super().__init__(groups)
        self.observer = observer
        self.rect = pg.Rect(0, 0, 64, 64).move(x, y)
        self.image = __class__.image
        self.hp = 30
        self.speed = 200
        self.vx, self.vy = 0, 0
        self.damage = 30
        self.shuffle_time = random.uniform(0, 2 * math.pi)

    def update(self, dt):
        self.shuffle_time += dt
        if self.hp <= 0:
            self.observer.score(200)
            self.kill()
        if not config.GAME_RECT_EXTEND.contains(self.rect):
            self.kill()
        self.x += 75 * math.sin(2 * self.shuffle_time) * dt
        self.y += self.speed * dt
        self.rect = pg.Rect(self.x, self.y, 64, 64)
        # print(self.rect)
        return

    def collide(self, other, dt):
        other.health -= self.damage * dt
        return
