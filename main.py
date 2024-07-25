import sys
from time import sleep
import engine


def main():
    game_engine = engine.Engine(delay=0.1)
    game_engine.run()


main()
