from io import BytesIO

import pygame.image
from PIL.Image import Image
from pygame import Surface, Vector2

from lib.CollisionBox import CollisionBox
from lib.Entity import Entity
from lib.EntityAnimation import EntityAnimation

IDLE = 0
WALK = 1
SLASH = 2
CAST = 3
FRONT = 0
LEFT = 1
RIGHT = 2
BACK = 3


class HumanEntity(Entity):
    _action = 0
    _status = IDLE
    _animation: EntityAnimation
    _direction = BACK

    def __init__(self, pos: Vector2 = pygame.Vector2(0, 0), speed: float = 0, screen: Surface = None,
                 animation: EntityAnimation = None, collision_box: CollisionBox = CollisionBox(Vector2(0, 0))):
        with BytesIO() as byte_buffer:
            animation.get_walking_forward().save(byte_buffer, format="PNG")
            byte_buffer.seek(0)
            super().__init__(pos, speed, pygame.image.load(byte_buffer), screen, collision_box)
        self._animation = animation

    def walk_forward(self, distance: int = 1):
        if self._action != 0 and self._status != WALK:
            return
        self._action = 1
        if self._status != WALK:
            self._status = WALK
            self._animation.set_frame()
        self._direction = FRONT
        with BytesIO() as byte_buffer:
            self._animation.get_walking_forward().save(byte_buffer, format="PNG")
            byte_buffer.seek(0)
            self.set_image(pygame.image.load(byte_buffer))
        self.move(0, -distance)

    def walk_left(self, distance: int = 1):
        if self._action != 0 and self._status != WALK:
            return
        self._action = 1
        if self._status != WALK:
            self._status = WALK
            self._animation.set_frame()
        self._direction = LEFT
        with BytesIO() as byte_buffer:
            self._animation.get_walking_left().save(byte_buffer, format="PNG")
            byte_buffer.seek(0)
            self.set_image(pygame.image.load(byte_buffer))
        self.move(-distance, 0)

    def walk_back(self, distance: int = 1):
        if self._action != 0 and self._status != WALK:
            return
        self._action = 1
        if self._status != WALK:
            self._status = WALK
            self._animation.set_frame()
        self._direction = BACK
        with BytesIO() as byte_buffer:
            self._animation.get_walking_back().save(byte_buffer, format="PNG")
            byte_buffer.seek(0)
            self.set_image(pygame.image.load(byte_buffer))
        self.move(0, distance)

    def walk_right(self, distance: int = 1):
        if self._action != 0 and self._status != WALK:
            return
        self._action = 1
        if self._status != WALK:
            self._status = WALK
            self._animation.set_frame()
        self._direction = RIGHT
        with BytesIO() as byte_buffer:
            self._animation.get_walking_right().save(byte_buffer, format="PNG")
            byte_buffer.seek(0)
            self.set_image(pygame.image.load(byte_buffer))
        self.move(distance, 0)

    def idle(self):
        if self._status != IDLE:
            self._status = IDLE
            self._animation.set_frame()
        image: Image
        if self._direction == FRONT:
            image = self._animation.get_idle_front()
        elif self._direction == LEFT:
            image = self._animation.get_idle_left()
        elif self._direction == BACK:
            image = self._animation.get_idle_back()
        else:
            image = self._animation.get_idle_right()
        with BytesIO() as byte_buffer:
            image.save(byte_buffer, format="PNG")
            byte_buffer.seek(0)
            self.set_image(pygame.image.load(byte_buffer))

    def slash(self):
        if self._status != SLASH:
            if self._action != 0:
                return
            self._status = SLASH
            self._animation.set_frame()
        if self._action == 0:
            self._action = 5 * self._animation.get_speed()
        image: Image
        if self._direction == FRONT:
            image = self._animation.get_slash_front()
        elif self._direction == LEFT:
            image = self._animation.get_slash_left()
        elif self._direction == BACK:
            image = self._animation.get_slash_back()
        else:
            image = self._animation.get_slash_right()
        with BytesIO() as byte_buffer:
            image.save(byte_buffer, format="PNG")
            byte_buffer.seek(0)
            self.set_image(pygame.image.load(byte_buffer))

    def cast(self):
        if self._status != CAST:
            if self._action != 0:
                return
            self._status = CAST
            self._animation.set_frame()
        if self._action == 0:
            self._action = 6 * self._animation.get_speed()
        image: Image
        if self._direction == FRONT:
            image = self._animation.get_cast_front()
        elif self._direction == LEFT:
            image = self._animation.get_cast_left()
        elif self._direction == BACK:
            image = self._animation.get_cast_back()
        else:
            image = self._animation.get_cast_right()
        with BytesIO() as byte_buffer:
            image.save(byte_buffer, format="PNG")
            byte_buffer.seek(0)
            self.set_image(pygame.image.load(byte_buffer))

    def update(self):
        if self._action == 0:
            self._status = IDLE
            self.idle()
            self._action = 1
        elif self._status == SLASH:
            self.slash()
        elif self._status == CAST:
            self.cast()
        self._action -= 1
        super().update()

    def get_status(self):
        return self._status
