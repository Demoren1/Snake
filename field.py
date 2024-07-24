import os
class Field:
    def __init__(self, width = 640, height = 480, default = True):
        if default:
            width, height = os.popen('stty size', 'r').read().split()
            width = int(width)  // 2
            height = int(height) // 2
        self._field = [[' '] * height for _ in range(width)]
        self.add_boundaries()

    def add_boundaries(self):
        width, height = self.size()
        for x in range(width):
            self._field[x][0] = '#'
            self._field[x][height - 1] = '#'
        for y in range(height):
            self._field[0][y] = '#'
            self._field[width - 1][y] = '#'
    def size(self):
        return len(self._field), len(self._field[0])