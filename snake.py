class Snake:
    def __init__(self, pos):
        self.pos = (pos[0], pos[1])
        self.lenght = 1
        self.body = [self.pos, (pos[0], pos[1] - 1), (pos[0], pos[1] - 2)]
    def position(self):
        return (self.x, self.y)
    
    def get_body(self):
        return self.body

    def move(self, direction):
        if direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1
        elif direction == "up":
            self.y -= 1
        elif direction == "down":
            self.y += 1
        self.body.append((self.x, self.y))