import snake
import field
import random


class Reward:
    def __init__(self, game_field: field.Field, game_snake: snake.Snake):
        self._game_field = game_field
        self._game_snake = game_snake

        self.rewards = set()

    def update_snake_and_field(self, game_field: field.Field, game_snake: snake.Snake):
        self._game_field = game_field
        self._game_snake = game_snake

    def add_reward(self, quantity, game_field: field.Field, game_snake: snake.Snake):
        self.update_snake_and_field(game_field, game_snake)

        for _ in range(quantity):
            reward_pos = self._find_reward_place()
            self.rewards.add(reward_pos)

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

    def remove_reward(self, cur_snake_pos):
        self.rewards.remove(cur_snake_pos)

    def get_rewards(self):
        return self.rewards
