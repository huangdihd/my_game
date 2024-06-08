from typing import Callable, List

from pygame.event import Event
from pygame import Surface, Vector2
import pygame

from lib.Entity import Entity
from lib.Player import Player
from lib.CollisionBox import CollisionBox


class Game:
    screen: Surface
    running: bool = False
    _clock = pygame.time.Clock()
    _entities: List[Entity] = []
    _loaded_entities: List[Entity] = []
    fps: int = 180
    player: Player
    size: tuple[int, int]
    _updates: List[Callable[[], None]] = []
    _events: List[Callable[[Event], None]] = []
    name: str

    def __init__(self, name: str, player: Player, size: tuple[int, int]) -> None:
        self.name = name
        self.player = player
        self.size = size
        self.screen = pygame.display.set_mode(self.size, flags=pygame.RESIZABLE)
        self.player.set_screen(self.screen)
        self._entities.append(self.player)

    def on_update(self):
        def update_processor(processor: Callable[[], None]):
            def wrapper():
                self._updates.append(processor)
            return wrapper()
        return update_processor

    def on_event(self):
        def event_processor(processor: Callable[[Event], None]):
            def wrapper():
                self._events.append(processor)
            return wrapper()
        return event_processor

    def init(self, title: str = None) -> None:
        pygame.init()
        if title:
            pygame.display.set_caption(title)
        pygame.display.set_icon(pygame.image.load('resources/logo.png'))
        self.running = True

    def run(self) -> None:
        self.init(self.name)
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                self.event_processor(event)
            self._update()
            self.screen_update()
            pygame.display.update()
            self._clock.tick(self.fps)

    def add_entity(self, entity: Entity) -> None:
        entity.set_screen(self.screen)
        self._entities.append(entity)

    def _update(self) -> None:
        for processor in self._updates:
            processor()
        for entity in self._entities:
            if entity.collision_box.intersects(CollisionBox(Vector2(0, 0), point2=Vector2(
                    self.screen.get_width(), self.screen.get_height()))):
                if entity not in self._loaded_entities:
                    self._loaded_entities.append(entity)
            else:
                if entity in self._loaded_entities:
                    self._loaded_entities.remove(entity)

        for entity in self._loaded_entities:
            entity.update()

    def event_processor(self, event: Event) -> None:
        for processor in self._events:
            processor(event)

    def screen_update(self) -> None:
        self.screen.fill("purple")
        for entity in sorted(self._loaded_entities, key=lambda e: e.get_pos().y):
            entity.draw()

    def get_entities(self):
        return self._entities
