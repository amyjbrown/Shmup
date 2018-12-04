# Entities and various ingame things
# Should use class methods for setup and image loading
# Anim = {"State_name" = list<(<Surface>, time)>;
import pygame as pg

Vector2 = pg.math.Vector2()


# Actor base class and appropriate ActorGroup class


class Actor(pg.sprite.Sprite):
    """
    Base class designed for in game Actors
    Some basic functionality has been added, but on the whole this should be overloaded
    By design, Setup() MUST be called before initializing any game objects, this serves as the spot for
    asset loading

    CLASS DATA
    init_flag <bool>
    Flag of whether setup() has been called

    tilesheet_path <str>
    File path to where information has been stored in a <Optionally in a .json format>

    graph_rect <pygame.Rect>
    Canonical rect for size of graphical rectangle

    collide_rect <pygame.Rect>
    Canonical Rect for collision box

    animations <dict>
    A dictionary of animation state and states
    Of the form {"state_name" : ( (img_0, time_0), (img_1, time_1),,,)

    melee_damage <int>
    Melee damage to be dealt to player on collision

    max_health <int>
    starting health of Actor

    score <int>
    Score to be dispensed upon death

    INSTANCE DATA
    self.position <pygame.math.Vector2>
    Position coordinate

    collide_rect <pygame.Rect>
    Collision detection rectangle

    graph_rect <pygame.Rect>
    Graphical display and position rectangle

    frame <int>
    Index for current animation frame

    anim_state <str>
    Key for current animation dictionary

    anim_timer <float>
    Current time spent on frame in seconds

    frame_time <float>
    Time current frame will last in seconds

    health <float>
    current health of Actor

    is_alive <bool>
    bool indicating whether or not Actor's health is gone and death sequence has started
    CLASS METHODS
    TODO Write class Methods
    INSTANCE METHODS
    TODO Write Instance Methods
    """
    # Static Class Data
    init_flag = False
    observer = None
    tilesheet_path = None
    tile_sheet = None
    FRAME_TIME = 1 / 60
    graph_rect: pg.Rect() = None
    collide_rect: pg.Rect() = None
    animations = dict()
    melee_damage = int()
    max_health = int()

    # Classes
    def __init__(self, position: pg.math.Vector2, *groups):
        """
        Creates a new Abstract class
        :param position: Vector2 indicating position of Entity
        :param observer: Observer
        :param groups: Groups to add sprite to, passed to super() init
        """
        if not self.__class__.init_flag:
            raise RuntimeError("Class{} was initialized before setup() called".format(self.__class__))
        super(Actor, self).__init__(*groups)
        # Position and physics data
        self.position = position
        self.velocity = pg.math.Vector2()
        self.collide_rect = pg.Rect(self.__class__.collide_rect).move(*position)
        # Graphical data
        self.image = None
        self.graph_rect = pg.Rect(self.__class__.graph_rect).move(*position)
        self.frame = 0
        self.anim_state = "idle"
        self.anim_timer = 0
        self.max_frames = len(self.animations["idle"])
        # Gameplay data
        self.health = self.max_health
        self.is_alive = True
        pass

    @classmethod
    def is_setup(cls) -> bool:
        """
        Checks whether setup() has been called
        :return: bool, True is setup() previously called
        """
        return cls.init_flag

    @classmethod
    def setup(cls):
        """
        Performs initialization of the class static data;
        Must be called before initializing a new Actor, safe to call multiple times
        :return None
        """
        pass

    @classmethod
    def subscribe(cls, observer):
        cls.observer = observer

    def move(self, dx: pg.math.Vector2):
        """
        Updates all position values by change
        :param dx: Vector2 for change in position
        :return: None
        """
        self.position += dx
        self.graph_rect.move_ip(*dx)
        self.collide_rect.move_ip(*dx)
        return

    def update(self, dt):
        """
        Abstract update function for general AI and state change, should be overriden
        :param dt: Time delta for simulation
        :return: None
        """
        pass

    def collide(self, other):
        """
        Logic to be performed when collision is detected
        :param other: Entity that has collided with self
        :return: None
        """
        pass

    def animate(self, dt):
        """
        Updates the current frame of the animation, optionally kills-self when death
        :param dt: Time difference to be added to anim timer
        :return: None
        """
        self.anim_timer += dt
        if self.anim_timer > self.FRAME_TIME:
            self.frame += 1
            self.frame %= self.max_frames
        pass

    def fire(self):
        """
        Spawn appropriate bullet for class; makes call to Obsever
        :return: None
        """
        pass

    def on_death(self):
        """
        Logic to be performed upon death
        Does not Kill() and remove from spites; use to initialize death anim, drop loot, etc.
        :return: None
        """
        pass


class ActorGroup(pg.sprite.AbstractGroup):
    """
    Special ActorGroup to be utilized for drawing and updating
    """

    def __init__(self):
        super(ActorGroup, self).__init__()

    def draw(self, surface):
        """
        Draws all sprites onto Surface, using sprite.image for image and sprite.graph_rect for position
        :param surface: Surface to be drawn unto
        :return:
        """
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            self.spritedict[spr] = surface_blit(spr.image, spr.graph_rect)
        self.lostsprites = []


class Particle(pg.sprite.Sprite):
    def __init__(self, *groups):
        super(Particle, self).__init__()
        pass


def actor_collide(act1: Actor, act2: Actor) -> bool:
    """
    Callback function for collisions
    :param act1: Actor 1
    :param act2: Actor 2
    :return: Bool if actors collision rect collides
    """
    return act1.collide_rect.colliderect(act2.collide_rect)


class EntityManager:
    """
    EntityManager object to manage, draw and update the groups of entities
    """

    def __init__(self, entity_dict: dict):
        """
        Creates new Entity Manager
        :param entity_dict:
        """
        pass

    def setup(self):
        """
        Performs setup of various game objects
        :return:
        """
        pass

    def update(self, dt):
        """
        Performs update and game logic
        :param dt: Time delta for simulation
        :return: None
        """
        pass

    def spawn_entity(self, type: str, *args):
        """
        Spawns Entity of type type
        :param type: Entity name to be spawned
        :param args: arguements to be passed to Entity
        :return:
        """

    def spawn_particle(self, type: str, *args):
        """
        Spawns particle of type Type
        :param type: Particle type to be spawned
        :param args: args to pass to particle type
        :return:
        """
        pass

    def render(self, surface):
        """
        Renders elements onto surface
        :param surface: Surface to be drawn onto
        :return:
        """
        pass

    def audio_parse(self) -> list:
        """
        Pushes up list of audio elements for scope to utilize
        :return: List of sound objects for music to utilize
        """
        pass

    def clear_all(self):
        """
        Clears entire Sprite list
        :return:
        """
