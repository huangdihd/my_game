from typing import Callable

import pygame
from pygame import Vector2, Surface
from lib.CollisionBox import CollisionBox


class Entity:
    _pos: Vector2
    _screen: Surface
    _image: Surface
    _speed = 0
    collision_box: CollisionBox
    _updates: list[Callable[[], None]]

    def __init__(self, pos: Vector2 = Vector2(0, 0), speed: float = 0, image: Surface = None, screen: Surface = None,
                 collision_box: CollisionBox = CollisionBox(Vector2(0, 0)), view_collision_box: bool = False) -> None:
        if image is not None and screen is not None:
            self._screen = screen
            self._image = image
        self._pos = pos
        self._speed = speed
        self.collision_box = collision_box
        self.collision_box.set_pos(self._pos)
        self.view_collision_box = view_collision_box
        self._updates = []

    def move(self, x: int = 0, y: int = 0) -> None:
        self._pos.x += x * self._speed
        self._pos.y += y * self._speed
        self.collision_box.set_pos(self.get_pos())

    def move_to(self, pos: Vector2 = Vector2(0, 0)) -> None:
        self._pos = pos
        self.collision_box.set_pos(self.get_pos())

    def get_pos(self) -> Vector2:
        return self._pos

    def update(self) -> None:
        for update in self._updates:
            update()

    def on_update(self):
        def update_processor(processor: Callable[[], None]):
            def wrapper():
                self._updates.append(processor)

            return wrapper()

        return update_processor

    def draw(self, image: Surface = None, screen: Surface = None) -> None:
        if image is None:
            image = self._image
        if screen is None:
            screen = self._screen
        if image is not None and screen is not None:
            draw_pos = self.get_pos().copy()
            draw_pos.x -= self._image.get_width() / 2
            draw_pos.y -= self._image.get_height() / 2
            self._screen.blit(self._image, draw_pos)
        if self.view_collision_box:
            pygame.draw.rect(self._screen, (0, 0, 0),
                             (self.collision_box.get_abs_x1(),
                              self.collision_box.get_abs_y1(),
                              self.collision_box.width(),
                              self.collision_box.height()),
                             1)

    def set_image(self, image: Surface) -> None:
        self._image = image

    def set_screen(self, screen: Surface) -> None:
        self._screen = screen
