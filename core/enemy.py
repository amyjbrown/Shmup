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
        super().__init__(groups)
        self.observer = observer
        self.rect = pg.Rect(0, 0, 64, 64).move(x, y)
        self.image = __class__.image
        self.hp = 30
        self.speed = 70
        self.vx, self.vy = 0, 0
        self.shuffle_time = 0

    def update(self, dt):
        if self.hp <= 0:
            self.observer.score(200)
            self.kill()
        if not config.GAME_RECT_EXTEND.contains(self.rect):
            self.kill()
        self.rect.move_ip(0, self.speed * dt)
        return

    def collide(self, other):
        print("Ouch, Daddy!")
