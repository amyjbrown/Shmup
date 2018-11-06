# Powerups
import pygame as pg


class HealthToken(pg.sprite.Sprite):
    image = pg.image.load("../Assets/Health Token.bmp")
    size_rect = pg.Rect(0, 0, 32, 32)
    image.set_colorkey(image.get_at((0, 0)))
    image.convert()

    def __init__(self, observer, x, y, *groups):
        super().__init__(*groups)
        self.observer = observer
        self.image = __class__.image
        self.rect = __class__.size_rect.move(x, y)
        self.speed = 60
        self.healing = 30

    def update(self, dt):
        self.rect.move_ip(0, self.speed * dt)

    def collide(self, other):
        t = other.hp + self.healing
        if t > 100:
            self.observer.score(5 * (t - 100))
            other.hp = 100
        else:
            other.hp += self.healing
        return
