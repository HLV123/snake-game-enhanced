# snake.py
"""Lớp Snake được tối ưu hóa với nhiều tính năng mới"""

from collections import deque
from game_object import GameObject
from constants import GRID_WIDTH, GRID_HEIGHT

class Snake:
    """Đại diện cho con rắn trong game với các tính năng nâng cao."""
    
    def __init__(self, initial_x, initial_y, wall_mode=True):
        """
        Khởi tạo rắn.
        wall_mode: True = chết khi đụng tường, False = xuyên tường
        """
        self.body = deque()
        self.wall_mode = wall_mode
        
        # Tạo thân rắn ban đầu (3 đoạn)
        for i in range(3):
            segment_type = 'snake_head' if i == 0 else 'snake_body'
            segment = GameObject(initial_x - i, initial_y, segment_type)
            self.body.append(segment)
            
        self.direction = 'RIGHT'
        self.next_direction = 'RIGHT'  # Để tránh xung đột khi bấm phím nhanh
        self.is_alive = True
        self.growth_pending = 0  # Số đoạn cần tăng

    def set_direction(self, direction):
        """Đặt hướng di chuyển cho rắn, ngăn di chuyển ngược lại."""
        opposite_directions = {
            'UP': 'DOWN',
            'DOWN': 'UP',
            'LEFT': 'RIGHT',
            'RIGHT': 'LEFT'
        }
        
        if direction in opposite_directions:
            if direction != opposite_directions.get(self.direction):
                self.next_direction = direction

    def move(self):
        """Di chuyển rắn theo hướng hiện tại."""
        if not self.is_alive:
            return
            
        # Cập nhật hướng
        self.direction = self.next_direction
        
        # Lấy vị trí đầu hiện tại
        head = self.body[0]
        new_x, new_y = head.x, head.y

        # Tính toán vị trí mới
        if self.direction == 'UP':
            new_y -= 1
        elif self.direction == 'DOWN':
            new_y += 1
        elif self.direction == 'LEFT':
            new_x -= 1
        elif self.direction == 'RIGHT':
            new_x += 1

        # Xử lý xuyên tường nếu cần
        if not self.wall_mode:
            new_x = new_x % GRID_WIDTH
            new_y = new_y % GRID_HEIGHT

        # Tạo đầu mới
        new_head = GameObject(new_x, new_y, 'snake_head')
        
        # Chuyển đầu cũ thành thân
        if self.body:
            self.body[0].obj_type = 'snake_body'
            
        # Thêm đầu mới
        self.body.appendleft(new_head)

        # Xử lý tăng trưởng
        if self.growth_pending > 0:
            self.growth_pending -= 1
        else:
            # Bỏ đuôi nếu không có tăng trưởng
            self.body.pop()

    def grow(self, segments=1):
        """Tăng chiều dài của rắn."""
        self.growth_pending += segments

    def check_collision(self):
        """Kiểm tra va chạm với tường hoặc với chính nó."""
        if not self.is_alive:
            return
            
        head = self.body[0]
        
        # Kiểm tra va chạm tường (chỉ khi wall_mode = True)
        if self.wall_mode:
            if (head.x < 0 or head.x >= GRID_WIDTH or 
                head.y < 0 or head.y >= GRID_HEIGHT):
                self.is_alive = False
                return

        # Kiểm tra va chạm với thân (bỏ qua đầu)
        head_pos = head.get_position()
        for i in range(1, len(self.body)):
            if head_pos == self.body[i].get_position():
                self.is_alive = False
                return

    def get_head_position(self):
        """Trả về vị trí của đầu rắn."""
        if self.body:
            return self.body[0].get_position()
        return None

    def get_body_positions(self):
        """Trả về danh sách tất cả vị trí của thân rắn."""
        return [segment.get_position() for segment in self.body]

    def draw(self, canvas):
        """Vẽ con rắn lên canvas."""
        for segment in self.body:
            segment.draw(canvas)
            
    def reset(self, initial_x, initial_y):
        """Reset rắn về trạng thái ban đầu."""
        self.body.clear()
        
        # Tạo lại thân rắn
        for i in range(3):
            segment_type = 'snake_head' if i == 0 else 'snake_body'
            segment = GameObject(initial_x - i, initial_y, segment_type)
            self.body.append(segment)
            
        self.direction = 'RIGHT'
        self.next_direction = 'RIGHT'
        self.is_alive = True
        self.growth_pending = 0