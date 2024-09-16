class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def move(self, dx: int, dy: int):
    self.x += dx
    self.y += dy

def __eq__(self, other: 'Point') -> bool:
    if not isinstance(other, Point):
        return False
    return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

