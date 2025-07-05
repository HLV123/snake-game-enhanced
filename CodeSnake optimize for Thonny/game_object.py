# game_object.py
"""Lớp cơ sở cho tất cả các đối tượng trong game"""

from constants import CELL_SIZE, COLORS

class GameObject:
    """Lớp cơ sở cho tất cả các đối tượng trong game."""
    
    def __init__(self, x, y, obj_type='default'):
        self.x = x
        self.y = y
        self.obj_type = obj_type
        self.visible = True

    def get_position(self):
        """Trả về vị trí hiện tại của đối tượng."""
        return (self.x, self.y)
    
    def set_position(self, x, y):
        """Đặt vị trí mới cho đối tượng."""
        self.x = x
        self.y = y

    def draw(self, canvas):
        """Vẽ đối tượng lên canvas - phương thức cơ sở."""
        if not self.visible:
            return False
            
        try:
            x1 = self.x * CELL_SIZE
            y1 = self.y * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            
            # Vẽ theo loại đối tượng
            if self.obj_type == 'snake_head':
                self._draw_snake_head(canvas, x1, y1, x2, y2)
            elif self.obj_type == 'snake_body':
                self._draw_snake_body(canvas, x1, y1, x2, y2)
            elif self.obj_type == 'normal_food':
                self._draw_normal_food(canvas, x1, y1, x2, y2)
            elif self.obj_type == 'special_food':
                self._draw_special_food(canvas, x1, y1, x2, y2)
            return True
        except Exception:
            return False

    def _draw_snake_head(self, canvas, x1, y1, x2, y2):
        """Vẽ đầu rắn với gradient effect."""
        # Vẽ hình chữ nhật chính
        canvas.create_rectangle(
            x1 + 1, y1 + 1, x2 - 1, y2 - 1,
            fill=COLORS['snake_head'],
            outline=COLORS['snake_outline'],
            width=2
        )
        # Thêm highlight
        canvas.create_rectangle(
            x1 + 3, y1 + 3, x2 - 3, y2 - 3,
            fill='#66ff66',
            outline=''
        )

    def _draw_snake_body(self, canvas, x1, y1, x2, y2):
        """Vẽ thân rắn."""
        canvas.create_rectangle(
            x1 + 2, y1 + 2, x2 - 2, y2 - 2,
            fill=COLORS['snake_body'],
            outline=COLORS['snake_outline'],
            width=1
        )

    def _draw_normal_food(self, canvas, x1, y1, x2, y2):
        """Vẽ đồ ăn bình thường."""
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        radius = CELL_SIZE // 3
        
        # Vẽ hình tròn với shadow effect
        canvas.create_oval(
            center_x - radius + 2, center_y - radius + 2,
            center_x + radius + 2, center_y + radius + 2,
            fill='#aa0000', outline=''
        )
        canvas.create_oval(
            center_x - radius, center_y - radius,
            center_x + radius, center_y + radius,
            fill=COLORS['normal_food'],
            outline='#cc0000',
            width=2
        )
        # Highlight
        canvas.create_oval(
            center_x - radius//2, center_y - radius//2,
            center_x + radius//3, center_y + radius//3,
            fill='#ff8888', outline=''
        )

    def _draw_special_food(self, canvas, x1, y1, x2, y2):
        """Vẽ đồ ăn đặc biệt với hiệu ứng lấp lánh."""
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        
        # Vẽ ngôi sao 5 cánh
        points = []
        import math
        for i in range(10):
            angle = math.pi * i / 5
            if i % 2 == 0:
                r = CELL_SIZE // 2.5
            else:
                r = CELL_SIZE // 5
            x = center_x + r * math.cos(angle - math.pi/2)
            y = center_y + r * math.sin(angle - math.pi/2)
            points.extend([x, y])
        
        # Shadow
        shadow_points = [p + 2 for p in points]
        canvas.create_polygon(shadow_points, fill='#cc8800', outline='')
        
        # Ngôi sao chính
        canvas.create_polygon(points, fill=COLORS['special_food'], outline='#ffaa00', width=2)
        
        # Thêm hiệu ứng lấp lánh
        canvas.create_oval(
            center_x - 3, center_y - 3, center_x + 3, center_y + 3,
            fill='#ffffff', outline=''
        )