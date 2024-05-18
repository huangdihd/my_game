import pygame
from pygame import Vector2, Surface


class Entity:
    _pos: Vector2
    _screen: Surface
    _image: Surface
    _speed = 0

    def __init__(self, pos: Vector2 = pygame.Vector2(0, 0), speed: float = 0, image: Surface = None, screen: Surface = None) -> None:
        if image is not None and screen is not None:
            self._screen = screen
            self._image = image
        self._pos = pos
        self._speed = speed

    def move(self, x: int = 0, y: int = 0) -> None:
        self._pos.x += x * self._speed
        self._pos.y += y * self._speed

    def move_to(self, pos: Vector2 = pygame.Vector2(0, 0)) -> None:
        self._pos = pos

    def get_pos(self) -> Vector2:
        return self._pos

    def draw(self, image: Surface = None, screen: Surface = None):
        if image is None:
            image = self._image
        if screen is None:
            screen = self._screen
        if image is not None and screen is not None:
            draw_pos = self.get_pos().copy()
            draw_pos.x -= self._image.get_width() / 2
            draw_pos.y -= self._image.get_height() / 2
            self._screen.blit(self._image, draw_pos)

    def set_image(self, image: Surface):
        self._image = image

    def set_screen(self, screen: Surface):
        self._screen = screen
