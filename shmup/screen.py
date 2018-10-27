import math
import pygame
# import os
import math


class Background:
    def __init__(self, surface: pygame.Surface, im: str, r: pygame.Rect, speed: float = 0.7):
        """
        Class that holds Background subsurface and scrolling method, as well as prologue lead out
        :param surface: Surface to be subsurfaced
        :param r: Rectangle area to be used as scrolling surface
        :param im: Image filepath to be used for background image
        :param speed: Speed in pixels updated per frame Positive scrolls up, negative scrolls down
        """
        self.surface = surface.subsurface(r)
        self.im = pygame.image.load(im)  # Creates surface
        self.w, self.h = self.im.get_size()
        self.x = 0
        self.y1 = 0
        self.y2 = -self.h
        self.speed = speed

    def scroll(self) -> None:
        """
        Procedure
        Scrolls the background in the play area
        """
        self.y1 += self.speed
        self.y2 += self.speed
        # print(self.y1); print(self.y2)
        self.surface.blit(self.im.convert(), (self.x, self.y1))
        self.surface.blit(self.im.convert(), (self.x, self.y2))
        if self.y1 > self.h:
            self.y1 = -self.h
        if self.y2 > self.h:
            self.y2 = -self.h
        return

    def prolog(self):
        pass


class GUI:
    pass


# Testing Scroll

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400, 640))
    bg = Background(surface=screen,
                    im='C:/Users/Jonathan/PycharmProjects/shmup/Assets/BG1.bmp',
                    r=pygame.Rect(0, 0, 400, 640))
    Game = True
    Clock = pygame.time.Clock()
    while Game:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bg.speed = float(input("Enter new Speed: "))
            elif event.type == pygame.QUIT:
                Game = False
        bg.scroll()
        pygame.display.flip()
        Clock.tick(60)
