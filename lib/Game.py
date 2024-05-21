from typing import Callable

from pygame.event import Event

from pygame import Surface

from lib.Entity import Entity
from lib.Player import Player

import pygame


class Game:
    screen: Surface
    running = False
    _clock = pygame.time.Clock()
    _entities: list[Entity] = []
    fps: int = 180
    player: Player
    size: tuple[int, int]
    _updates: list[Callable[[], None]] = []
    _events: list[Callable[[Event], None]] = []
    name: str

    def __init__(self, name: str, player: Player, size: tuple[int, int]):
        self.name = name
        self.player = player
        self.size = size
        self.screen = pygame.display.set_mode(self.size, flags=pygame.RESIZABLE)
        self.player.set_screen(self.screen)
        self._entities.append(self.player)

    def on_update(self, processor: Callable[[], None]):
        self._updates.append(processor)

    def on_event(self, processor: Callable[[Event], None]):
        self._events.append(processor)

    def init(self, title: str = None):
        pygame.init()
        pygame.display.set_caption(title)
        pygame.display.set_icon(pygame.image.load('resources/logo.png'))
        self.running = True

    def run(self):
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

    def add_entity(self, entity: Entity):
        entity.set_screen(self.screen)
        self._entities.append(entity)
        entity.set_all_entities(self._entities)

    def _update(self):
        for processor in self._updates:
            processor()

    def event_processor(self, event: Event):
        for processor in self._events:
            processor(event)

    def screen_update(self):
        self.screen.fill("purple")
        for entity in sorted(self._entities, key=lambda e: e.get_pos().y):
            entity.draw()

    def get_entities(self):
        return self._entities
