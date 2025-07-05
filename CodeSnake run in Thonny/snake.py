# snake.py

from collections import deque
from game_object import GameObject

class Snake:
    """Đại diện cho con rắn trong game."""
    def __init__(self, initial_x, initial_y):
        self.body = deque([GameObject(initial_x - i, initial_y, '#') for i in range(3)])
        # Đánh dấu đầu rắn
        self.body[0].is_head = True
        self.direction = 'RIGHT'
        self.is_alive = True

    def set_direction(self, direction):
        """Đặt hướng di chuyển cho rắn, ngăn di chuyển ngược lại."""
        if direction == 'UP' and self.direction != 'DOWN':
            self.direction = direction
        elif direction == 'DOWN' and self.direction != 'UP':
            self.direction = direction
        elif direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = direction
        elif direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = direction

    def move(self):
        """Di chuyển rắn theo hướng hiện tại."""
        head = self.body[0]
        new_x, new_y = head.x, head.y

        if self.direction == 'UP':
            new_y -= 1
        elif self.direction == 'DOWN':
            new_y += 1
        elif self.direction == 'LEFT':
            new_x -= 1
        elif self.direction == 'RIGHT':
            new_x += 1

        new_head = GameObject(new_x, new_y, '#')
        new_head.is_head = True
        
        # Bỏ đánh dấu đầu cũ
        if self.body:
            self.body[0].is_head = False
            
        self.body.appendleft(new_head)
        self.body.pop()

    def grow(self):
        """Tăng chiều dài của rắn."""
        tail = self.body[-1]
        new_segment = GameObject(tail.x, tail.y, '#')
        self.body.append(new_segment)

    def check_collision(self, width, height):
        """Kiểm tra va chạm với tường hoặc với chính nó."""
        head = self.body[0]
        
        # Va chạm tường
        if head.x < 0 or head.x >= width or head.y < 0 or head.y >= height:
            self.is_alive = False
            return

        # Va chạm với thân
        for i in range(1, len(self.body)):
            if head.get_position() == self.body[i].get_position():
                self.is_alive = False
                return

    def draw(self, canvas, cell_size):
        """Vẽ con rắn lên canvas."""
        for segment in self.body:
            segment.draw(canvas, cell_size)