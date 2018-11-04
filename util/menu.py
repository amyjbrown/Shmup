# Class for menu, pause menu, and menu widgets
# TODO Widget, Menu, Pause Menu Scene
import scene


class ButtonWidget:
    """
    Base class for MenuWidget elements and GUI elements
    """

    def __init__(self, text, fun: function):
        self.text = text
        self.fun = fun
        return

    def draw(self):
        pass

    def enter(self):
        self.fun()


class Menu(scene.Scene):
    """
    A Menu Scene
    """

    def __init__(self):
        super(Menu, self).__init__()
        self.back = None  #
        self.location = 0
        self.widgets = ["Play Game"]
