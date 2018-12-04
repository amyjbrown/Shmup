# GUI Object
# Holds GUI info and updates


class GUI:
    """
    Class for GUI object
    """

    def __init__(self):
        self.updating = False
        self.health = 0
        self.lives = 0
        self.lives = 0
        self.high_score = 0
        self.rank = 0
        self.missiles = 0
        self.bomb = 0
        self.backgrond = 0

    def update(self, dt):
        pass

    def hook(self):
        pass

    def draw(self, surface):
        pass
