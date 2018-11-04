# Scene and Scene management objects
# Scene treated as quasi FSM
# import shmup
import pygame as pg


class Scene:

    """
    Abstract Scene class to be overloaded; any core data should be placed in here
    Interface and state holder for individual game scene
    Self.next should default to None
    Contains a parse input, update and render method
    """
    def __init__(self, **settings):
        """
        Use to initialize an individual scene; use this for settup and loading
        Self.next should default to none initially
        :param settings: settings to be passed to an individual scene for setup
        """
        self.final: bool = False # Use for quitting main game_loop
        self.next: str = None  # Use for setting next element
        self.next_params: dict = False
        return

    def parse_input(self, *events):
        """
        <PRO> Parses a set of events taken externally
        :param events: event list to be utilized for parsing
        :return: None
        """
        pass

    def update(self, dt):
        """
        <PRO> Updates simulation by one frame
        :param dt: time-delta used for simulation
        :return: None
        """
        pass

    def set_next(self, **params):
        """
        <MUT> Use this set appropriate params for next state
        :return: None
        """
        self.next = True
        self.next_params = params

    def render(self, surface):
        """
        Renders state of scene onto surface
        Main display surface for normal game
        :return:
        """
        pass


class SceneManager:

    """
    A Singleton Scene Manager, used to hold and run the main game loop
    Try to decouple this as strongly from scenes as possible - they don't need to know their maker
    """

    def __init__(self, scene_dict: dict, initial: str, display, event_manager, audio_manager):
        """
        Initializes State Machine
        :param scene_dict: str -> Scene mapping for states
        :param initial: string token of initial scene
        :param settings various settings for setup
        """
        self.current_id: str = initial
        self.scenes: dict = scene_dict
        self.current_scene: Scene = self.scenes[self.current_id]()
        self.display = display
        self.event_manager = event_manager
        self.audio_maanger = audio_manager
        return

    def swap_scene(self, next_scene: str, settings: dict):
        """
        <MUT> Attempts to load in new_scene, will raise Error if not
        :param next_scene:
        :param settings: dict of settings to be passed to the new scene
        :return:
        """
        new = self.scenes.get(next_scene) # gets new Scene typeobject
        if new is None:  # Error Checking to be let us know when and where what went wrong
            raise ValueError("{} attempted to load undefined {} with params {}"\
                .format(self.current_scene, next_scene, settings)
            )
        new = new(**settings)  # Initializes new Scene
        self.current_scene = new  # Finally, mutates current scene to new_scene
        return

    def main_loop(self):
        """
        <PRO> Runs the main gameloop for the set of scenes we have
        Utilizes scene.next for State Transitioning and Scene.final for exit cleanup
        :return: NONE
        """
        # Game utilities outside of the structure
        clock = pg.time.Clock()
        # While Game
        while not self.current_scene.final:
            dt = clock.Tick(60) / 1000  # Takes dt and locks max framerate at 60
            self.current_scene.parse_input(self.event_manager.get())
            self.current_scene.update(dt)
            if self.current_scene.next:  # check here so no one-frame lag of loading new scene
                self.swap_scene(self.current_scene.next, self.current_scene.next_params)
            self.current_scene.render(self.display)
        # Once we reach scene.final, we do end/cleanup
        return

