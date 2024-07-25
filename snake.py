import sys

class Snake:
    def __init__(self, pos):
        self._pos = (pos[0], pos[1])
        self._lenght = 3
        self._body = [self._pos, (pos[0], pos[1] - 1), (pos[0], pos[1] - 2)]
        self._direction = "right"

    def get_position(self):
        return (self._pos[0], self._pos[1])

    def get_body(self):
        return self._body

    def move(self):
        if self._direction == "right":
            self._pos = (self._pos[0], self._pos[1] + 1)
        if self._direction == "left":
            self._pos = (self._pos[0], self._pos[1] - 1)
        if self._direction == "up":
            self._pos = (self._pos[0] + 1, self._pos[1])
        if self._direction == "down":
            self._pos = (self._pos[0] - 1, self._pos[1] + 1)
        self._body.insert(0, self._pos)
        if len(self._body) > self._lenght:
            self._body.pop()

    def check_collision(self, game_field_size):
        if (
            self._pos[0] < 0
            or self._pos[0] >= game_field_size[0]
            or self._pos[1] < 0
            or self._pos[1] >= game_field_size[1]
        ):
            sys.exit(0)
        if self._body.count(self._pos) > 1:
            sys.exit(0)
    def grow(self):
        self._lenght += 1
        self._body.append(self._pos)
