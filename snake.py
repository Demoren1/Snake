import sys
import field

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

    def get_lenght(self):
        return self._lenght

    def move(self):
        if self._direction == "right":
            self._pos = (self._pos[0], self._pos[1] + 1)
        if self._direction == "left":
            self._pos = (self._pos[0], self._pos[1] - 1)
        if self._direction == "up":
            self._pos = (self._pos[0] - 1, self._pos[1])
        if self._direction == "down":
            self._pos = (self._pos[0] + 1, self._pos[1])
        self._body.insert(0, self._pos)
        if len(self._body) > self._lenght:
            self._body.pop()

    def check_collision(self, game_field_size):
        if (
            self._pos[0] < 1
            or self._pos[0] >= game_field_size[0] - 1
            or self._pos[1] < 1
            or self._pos[1] >= game_field_size[1] - 1
        ):
            sys.exit(0)
        if self._body.count(self._pos) > 1:
            sys.exit(0)

    def check_reward_collision(self, rewards):
        if self._pos in rewards:
            return 1, self._pos
        
        return 0, self._pos


    def grow(self):
        self._lenght += 1
        self._body.append(self._pos)

    def set_direction(self, direction):
        if direction == "right" and self._direction != "left":
            self._direction = direction
        if direction == "left" and self._direction != "right":
            self._direction = direction
        if direction == "up" and self._direction != "down":
            self._direction = direction
        if direction == "down" and self._direction != "up":
            self._direction = direction
