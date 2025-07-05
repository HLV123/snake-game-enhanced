# food.py

import random
from game_object import GameObject

class Food(GameObject):
    """Đại diện cho mồi trong game."""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        super().__init__(x, y, '*')

    def respawn(self, snake_body):
        """Tạo lại mồi ở vị trí mới không trùng với rắn."""
        while True:
            self.x = random.randint(0, self.width - 1)
            self.y = random.randint(0, self.height - 1)
            if (self.x, self.y) not in [(segment.x, segment.y) for segment in snake_body]:
                break

    def draw(self, canvas, cell_size):
        """Vẽ mồi lên canvas."""
        super().draw(canvas, cell_size)