import field 
import snake
import sys
import random
from time import sleep

class Engine:
    def __init__(self, delay = 1, width = 640, height = 480, default = True,):
        self.game_field = field.Field(width, height, default)
        self.delay = delay
        self.game_snake = snake.Snake([x // 2 for x in self.game_field.size()])

    def draw(self):
        snake_body = self.game_snake.get_body()
        field_size = self.game_field.size()

        for x in range(field_size[0]):
            for y in range(field_size[1]):
                if (x, y) in snake_body:
                    if snake_body[0] == (x, y):
                        print("@", end = "")
                    else:
                        print("o", end = "")
                else:
                    print(self.game_field._field[x][y], end = "")
            print("")
        sleep(self.delay)
    def run(self):
        while True:
            self.draw()