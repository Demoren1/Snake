import snake
import field
import random


class Reward:
    def __init__(self, game_field : field.Field, game_snake : snake.Snake):
        self._game_field = game_field
        self._game_snake = game_snake

    def add_reward(self):
        reward_pos = self._find_reward_place()
        self._game_field._field[reward_pos[0]][reward_pos[1]] = "+"

    def _find_reward_place(self):
        reward_pos = random.choice(
            [
                (x, y)
                for x in range(1, self._game_field.size()[0] - 1)
                for y in range(1, self._game_field.size()[1] - 1)
                if not self._game_snake.get_body().count((x, y))
            ]
        )

        return reward_pos
