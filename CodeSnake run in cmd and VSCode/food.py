# food.py

import random
from game_object import GameObject

class Food(GameObject):
    """Đại diện cho mồi trong game."""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        super().__init__(x, y, '*')

    def respawn(self, snake_body):
        """Tạo lại mồi ở vị trí mới không trùng với rắn."""
        while True:
            self.x = random.randint(1, self.width - 2)
            self.y = random.randint(1, self.height - 2)
            if (self.x, self.y) not in [(segment.x, segment.y) for segment in snake_body]:
                break