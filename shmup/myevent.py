# myevent
# implements custom user commands allowing for key rebinding
import pygame as pg


class Event:

    """
    custom event container class
    """
    def __init__(self, key, type, down):
        self.type = type
        self.key = key
        self.down = down
        self.up = not down
        return


class EventManager:

    """
    Event Manager class is a wrapper that initializes the Pygame Events -> Custom Event Keys
    Should work like pygame Events does
    """

    def __init__(self, keys, key_map=None):
        """

        :param keys: Custom Key tokens to be added
        :param key_map: Map of Custom Event Str tokens -> PG Keys, to be repacked in it
        """
        self.buttons = keys
        self.pressed = dict()
        self.key_map = dict()
        # Initialize allows for multiple keys to map to commands
        for custom in key_map:
            for pygame_key in key_map[custom]:
                self.key_map[pygame_key] = custom
        # for python _pressed method
        for b in keys:
            self.pressed[b] = False
        # Creates forbidden keys
        pg.event.set_allowed(None)  # Blocks all keys except for keys I push in
        pg.event.set_allowed(self.key_map.keys())  # Allows all keys that have custom mapping
        pg.event.set_allowed(pg.QUIT)  # Also adds omni useful QUIT
        return

    def reset_map(self, key_map):
        pass

    def get(self)->list:
        """
        Maps pygame.event.get() list t custom event list
        :return: List of custom Events
        """
