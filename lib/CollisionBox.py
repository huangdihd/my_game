from copy import copy

from pygame import Vector2


class CollisionBox:
    def __init__(self,pos:  Vector2, point1: Vector2 = Vector2(0, 0), point2: Vector2 = Vector2(0, 0)):
        self.point1 = point1
        self.point2 = point2
        self.pos = pos

    def width(self) -> float:
        return abs(self.point2.x - self.point1.x)

    def height(self) -> float:
        return abs(self.point2.y - self.point1.y)

    def area(self) -> float:
        return self.width() * self.height()

    def contains(self, point: Vector2) -> bool:
        min_x = min(self.point1.x, self.point2.x) + self.pos.x
        max_x = max(self.point1.x, self.point2.x) + self.pos.x
        min_y = min(self.point1.y, self.point2.y) + self.pos.y
        max_y = max(self.point1.y, self.point2.y) + self.pos.y

        return min_x <= point.x <= max_x and min_y <= point.y <= max_y

    def intersects(self, other: 'CollisionBox') -> bool:
        return not (self.get_abs_x2() < other.get_abs_x1() or
                    self.get_abs_x1() > other.get_abs_x2() or
                    self.get_abs_y2() < other.get_abs_y1() or
                    self.get_abs_y1() > other.get_abs_y2())

    def set_pos(self, pos: Vector2) -> None:
        self.pos = pos

    def get_abs_x1(self) -> float:
        return self.point1.x + self.pos.x

    def get_abs_x2(self) -> float:
        return self.point2.x + self.pos.x

    def get_abs_y1(self) -> float:
        return self.point1.y + self.pos.y

    def get_abs_y2(self) -> float:
        return self.point2.y + self.pos.y

    def copy(self):
        return copy(self)
