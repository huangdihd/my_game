from PIL import Image
import os


class EntityAnimation:
    _images: []
    _frame = 0
    _speed: int

    def __init__(self, animation_dir: str, speed: int):
        self._images = []
        self._speed = speed
        walk_image_path = os.path.join(animation_dir, 'walk.png')
        self._load_little_animation(walk_image_path)
        idle_image_path = os.path.join(animation_dir, 'idle.png')
        self._load_little_animation(idle_image_path)
        slash_image_path = os.path.join(animation_dir, 'slash.png')
        self._load_large_animation(slash_image_path)
        cast_image_path = os.path.join(animation_dir, 'cast.png')
        self._load_little_animation(cast_image_path)

    def get_speed(self):
        return self._speed

    def _load_little_animation(self, image_path: str):
        image = Image.open(open(image_path, 'rb'))
        size = image.size
        for line in range(4):
            self._images.append(
                [image.crop((i * 64, line * 64, (i + 1) * 64, (line + 1) * 64)) for i in range(size[0] // 64)])

    def _load_large_animation(self, image_path: str):
        image = Image.open(open(image_path, 'rb'))
        size = image.size
        for line in range(4):
            self._images.append(
                [image.crop((i * 192, line * 192, (i + 1) * 192, (line + 1) * 192)) for i in range(size[0] // 192)])

    def set_frame(self, frame: int = 0):
        self._frame = frame

    def get_walking_forward(self, frame: int = -1) -> Image:
        if frame == -1:
            self._frame += 1
            self._frame %= 8 * self._speed
            frame = self._frame
        frame %= 8 * self._speed
        return self._images[0][frame // self._speed]

    def get_walking_left(self, frame: int = -1) -> Image:
        if frame == -1:
            self._frame += 1
            self._frame %= 8 * self._speed
            frame = self._frame
        frame %= 8 * self._speed
        return self._images[1][frame // self._speed]

    def get_walking_back(self, frame: int = -1) -> Image:
        if frame == -1:
            self._frame += 1
            self._frame %= 8 * self._speed
            frame = self._frame
        frame %= 8 * self._speed
        return self._images[2][frame // self._speed]

    def get_walking_right(self, frame: int = -1) -> Image:
        if frame == -1:
            self._frame += 1
            self._frame %= 8 * self._speed
            frame = self._frame
        frame %= 8 * self._speed
        return self._images[3][frame // self._speed]

    def get_idle_front(self, frame: int = -1) -> Image:
        if frame == -1:
            self._frame += 1
            self._frame %= 8 * self._speed
            frame = self._frame
        frame %= 8 * self._speed
        return self._images[4][frame // (self._speed * 4)]

    def get_idle_left(self, frame: int = -1) -> Image:
        if frame == -1:
            self._frame += 1
            self._frame %= 8 * self._speed
            frame = self._frame
        frame %= 8 * self._speed
        return self._images[5][frame // (self._speed * 4)]

    def get_idle_back(self, frame: int = -1) -> Image:
        if frame == -1:
            self._frame += 1
            self._frame %= 8 * self._speed
            frame = self._frame
        frame %= 8 * self._speed
        return self._images[6][frame // (self._speed * 4)]

    def get_idle_right(self, frame: int = -1) -> Image:
        if frame == -1:
            self._frame += 1
            self._frame %= 8 * self._speed
            frame = self._frame
        frame %= 8 * self._speed
        return self._images[7][frame // (self._speed * 4)]

    def get_slash_front(self, frame: int = -1) -> Image:
        if frame == -1:
            self._frame += 1
            self._frame %= 5 * self._speed
            frame = self._frame
        frame %= 5 * self._speed
        return self._images[8][frame // self._speed]

    def get_slash_left(self, frame: int = -1) -> Image:
        if frame == -1:
            self._frame += 1
            self._frame %= 5 * self._speed
            frame = self._frame
        frame %= 5 * self._speed
        return self._images[9][frame // self._speed]

    def get_slash_back(self, frame: int = -1) -> Image:
        if frame == -1:
            self._frame += 1
            self._frame %= 5 * self._speed
            frame = self._frame
        frame %= 5 * self._speed
        return self._images[10][frame // self._speed]

    def get_slash_right(self, frame: int = -1) -> Image:
        if frame == -1:
            self._frame += 1
            self._frame %= 5 * self._speed
            frame = self._frame
        frame %= 5 * self._speed
        return self._images[11][frame // self._speed]

    def get_cast_front(self, frame: int = -1) -> Image:
        if frame == -1:
            self._frame += 1
            self._frame %= 6 * self._speed
            frame = self._frame
        frame %= 6 * self._speed
        return self._images[12][frame // self._speed]

    def get_cast_left(self, frame: int = -1) -> Image:
        if frame == -1:
            self._frame += 1
            self._frame %= 6 * self._speed
            frame = self._frame
        frame %= 6 * self._speed
        return self._images[13][frame // self._speed]

    def get_cast_back(self, frame: int = -1) -> Image:
        if frame == -1:
            self._frame += 1
            self._frame %= 6 * self._speed
            frame = self._frame
        frame %= 6 * self._speed
        return self._images[14][frame // self._speed]

    def get_cast_right(self, frame: int = -1) -> Image:
        if frame == -1:
            self._frame += 1
            self._frame %= 6 * self._speed
            frame = self._frame
        frame %= 6 * self._speed
        return self._images[15][frame // self._speed]
