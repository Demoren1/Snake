import field
import snake
import reward
import sys
import os
import random
from time import sleep
from pynput import keyboard


class Engine:
    def __init__(
        self,
        delay=1,
        width=640,
        height=480,
        default=True,
    ):
        self.game_field = field.Field(width, height, default)
        self.delay = delay

        self.current_direction = "right"
        self.game_snake = snake.Snake([x // 2 for x in self.game_field.size()])
        self.game_snake.set_direction(self.current_direction)

        self.rewarder = reward.Reward(self.game_field, self.game_snake)

        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

        self.time = 0

    def draw(self, string):
        os.system("clear")

        snake_body = self.game_snake.get_body()
        field_size = self.game_field.size()

        for x in range(field_size[0]):
            for y in range(field_size[1]):
                if (x, y) in snake_body:
                    if snake_body[0] == (x, y):
                        print("@", end="")
                    else:
                        print("o", end="")
                elif (x, y) in self.rewarder.get_rewards():
                    print("+", end="")
                    pass
                else:
                    print(self.game_field._field[x][y], end="")
            print("")
        print(f"Score: {string}")
        sleep(self.delay)
        os.system("clear")

    def on_press(self, key):
        try:
            if key == keyboard.Key.up:
                self.current_direction = "up"
            elif key == keyboard.Key.down:
                self.current_direction = "down"
            elif key == keyboard.Key.left:
                self.current_direction = "left"
            elif key == keyboard.Key.right:
                self.current_direction = "right"
        except AttributeError:
            pass

    def run(self):
        current_score = self.game_snake.get_lenght()
        tmp_score = current_score

        grow_flag = False
        cur_snkae_pos = self.game_snake.get_position()

        self.rewarder.add_reward(20, self.game_field, self.game_snake)
        while True:
            self.time += 1

            self.draw(current_score)

            self.game_snake.set_direction(self.current_direction)
            self.game_snake.check_collision(self.game_field.size())

            grow_flag, cur_snkae_pos = self.game_snake.check_reward_collision(self.rewarder.get_rewards())
            if grow_flag:
                self.game_snake.grow()
                self.rewarder.remove_reward(cur_snkae_pos)

            tmp_score = self.game_snake.get_lenght()

            self.game_snake.move()

            if tmp_score != current_score:
                self.rewarder.add_reward(1, self.game_field, self.game_snake)
                current_score = tmp_score
