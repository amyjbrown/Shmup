# Class for menu, pause menu, and menu widgets
# TODO Widget, Menu, Pause Menu Scene
import scene

class Menu(scene.Scene):
    """
    A Menu Scene
    """

    def __init__(self):
        super(Menu, self).__init__()
        self.back = None  #
        self.location = 0
        self.widgets = ["Play Game"]
