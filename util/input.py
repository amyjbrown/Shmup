# myevent
# implements custom user commands allowing for key rebinding
import pygame as pg


class Event:
    """
    custom event container class
    """
    def __init__(self, key, down):
        self.key = key
        self.down = down
        self.up = not down
        return

    def __repr__(self):
        return "<Event Object {} Up:{} Down: {}".format(self.key, self.up, self.down)


class EventManager:

    """
    Event Manager class is a wrapper that initializes the Pygame Events -> Custom Event Keys
    Should work like pygame Events does
    """

    def __init__(self, buttons, key_map=None):
        """
        Initializes the Event manager with appropriate values
        :param keys: Custom Key tokens to be added
        :param key_map: Map of Custom Event Str tokens -> PG Keys, to be repacked in it
        """
        self.buttons = buttons  # Note QUIT is a special type here
        self.pressed = dict()
        self.key_map = dict()
        self.inputs = list()
        # Initialize allows for multiple keys to map to commands
        for custom in key_map:
            for pygame_key in key_map[custom]:
                self.key_map[pygame_key] = custom
        # for python _pressed method
        for b in buttons:
            self.pressed[b] = False
        print(self.pressed)
        # Sets values we are allowed to have as input
        self.inputs = list(self.key_map.keys())
        return

    def reset_map(self, key_map):
        pass

    def get(self)->list:
        """
        Maps pygame.event.get() list t custom event list
        :return: List of custom Events
        """
        # This impplicitly assumes that appropriate buttons will have blocked
        event_list = []
        for event in pg.event.get():
            if event.type == pg.QUIT:
                event_list.append(Event("QUIT", False))
            elif event.type == pg.KEYDOWN and event.key in self.inputs:
                key = self.key_map[event.key]
                event_list.append(Event(key, True))
                self.pressed[key] = True
            elif event.type == pg.KEYUP and event.key in self.inputs:
                key = self.key_map[event.key]
                event_list.append(Event(key, False))
                self.pressed[key] = False
        return event_list


# Now do initialization


# unit test
if __name__ == "__main__":
    display = pg.display.set_mode((200,200))
    keys = ["up", "down", "left", "right", "fire", "missile", "bomb", "menu"]
    # Keymap more to remind myself than anything else
    key_map = {"up": [pg.K_UP, pg.K_w],
               "down": [pg.K_DOWN, pg.K_s],
               "right": [pg.K_RIGHT, pg.K_d],
               "left": [pg.K_LEFT, pg.K_a],
               "menu": [pg.K_ESCAPE],
               "fire": [pg.K_SPACE],
               "missile": [pg.K_x],
               "bomb": [pg.K_z],
               }
    manager = EventManager(keys, key_map)
    test = True
    while test:
        events = manager.get()
        for event in events:
            print(event)
            if event.key is "QUIT" or event.key is "menu":
                test = False
