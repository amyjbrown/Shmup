# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)
import pygame as pg


# Experimental: don't touch to heavily
class Animation:
    def __init__(self, name: str, *images, repeat=False):
        self.name = name
        self.images = images
        self.repeat = repeat


class Spritesheet:
    """
    Spritesheet class for loading large images and loading individual sprites or lists of sprites
    """
    def __init__(self, filename):
        try:
            self.sheet = pg.image.load(filename).convert()
        except:
            raise pg.error("Path {} could not be reached or was invalid".format(filename))

    def get_image(self, rectangle, colorkey=None) -> pg.SurfaceType:
        """
        Load image at specified rectangle
        :param rectangle: (x,y, x+width, y + height) of image on sprite sheet
        :param colorkey: 3-tuple for transparent
        :return: Surface
        """
        rect = pg.Rect(rectangle)
        image = pg.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))  # Makes sure colorkey is defined is -1
            image.set_colorkey(colorkey, pg.RLEACCEL)
        return image

    def get_list(self, rects, colorkey=None) -> list:
        """
        Returns a list of Surfaces
        :param rects: iterable of Rect locations of images
        :param colorkey: Colorkey param for get_image
        :return:
        """
        return [self.get_image(rect, colorkey) for rect in rects]

    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey=None) -> list:
        """
        Makes a list of every rect-sizes image in one horizontal strip
        Will not work
        :param rect: Size of individual image
        :param image_count: number of images to load
        :param colorkey: Colorkey param to be passed to get_list()
        :return: List of Surfaces
        """
        tups = [(rect[0] + rect[2] * i, rect[1], rect[2], rect[3])
                for i in range(image_count)]
        return self.get_list(tups, colorkey)

    def full_load(self, rect) -> list:
        pass
