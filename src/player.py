# Player class
import pygame as pg

import config
import entities
import util


class Player(entities.Actor):
    Spritesheet = "../Assets/Ship.bmp"
    graph_rect = pg.Rect(0, 0, 64, 64)
    collide_rect = pg.Rect(0, 0, 64, 64)
    max_health = 100

    def __init__(self, position: pg.Vector2, *groups):
        super(Player, self).__init__(position, *groups)
        # cooldown - Frames between shots
        self.cooldown = 0
        self.COOLDOWN_MAX = 1 / 10
        # Fire side - used for alternating fire
        self.fire_side = False
        self.speed = 0
        return

    def update(self, dt):
        """
        TODO Rewrite this for new structure
        Prcoedure updates the module and all appropriate AI/elements
        :param dt: time interval for
        """
        # TODO collision detection to ensure does not move out of gamespace
        if config.GAME_RECT.contains(self.graph_rect.move(0, self.velocity.y * dt)):
            self.move(pg.Vector2(0, self.velocity.y))
        if config.GAME_RECT.contains(self.graph_rect.move(self.velocity.x * dt, 0)):
            self.move(pg.Vector2(self.velocity.x, 0))
        self.cooldown -= dt
        self.animate(dt)
        return

    @classmethod
    def setup(cls):
        if not cls.init_flag:
            cls.init_flag = True
            cls.tile_sheet = util.assetloader.Spritesheet(cls.tilesheet_path)
            cls.animations["idle"] = cls.tile_sheet.get_image(cls.graph_rect, colorkey=-1)

    def notify(self, entity, event):
        """
        MUT Sends notification method to observer
        """
        self.observer.on_notify(entity, event)
        pass

    def fire(self):
        """
        Sends Spawn Bullet to Observer
        :return:
        """
        if self.cooldown <= 0:
            self.observer.spawn("player bullet", self.position + pg.Vector2(20 + 8 * self.fire_side, -5))
            self.cooldown = self.COOLDOWN_MAX
            self.fire_side = not self.fire_side

    def on_death(self):
        pass

    def revive(self):
        """
        Revives and reinitializes the player after dying with more than a life left
        :return: None
        """
        self.health = self.max_health
        self.position = pg.Vector2(200, 200)
        self.cooldown = 0
