# input_manager.py
"""Quản lý input và xử lý sự kiện bàn phím"""

from constants import KEYS

class InputManager:
    """Quản lý input từ bàn phím."""
    
    def __init__(self):
        self.key_buffer = []
        self.last_direction_time = 0
        self.pause_pressed = False
        
    def handle_key_event(self, event):
        """Xử lý sự kiện bàn phím và thêm vào buffer."""
        key = event.keysym
        
        # Xử lý phím pause đặc biệt (chỉ trigger khi nhả phím)
        if key in KEYS['PAUSE']:
            if not self.pause_pressed:
                self.key_buffer.append('PAUSE')
                self.pause_pressed = True
        else:
            self.pause_pressed = False
            
        # Thêm các phím khác vào buffer
        if key not in KEYS['PAUSE']:
            self.key_buffer.append(key)
    
    def get_next_action(self):
        """Lấy action tiếp theo từ buffer."""
        if not self.key_buffer:
            return None
            
        key = self.key_buffer.pop(0)
        
        # Xác định action từ key
        if key == 'PAUSE':
            return 'PAUSE'
        elif key in KEYS['UP']:
            return 'UP'
        elif key in KEYS['DOWN']:
            return 'DOWN'
        elif key in KEYS['LEFT']:
            return 'LEFT'
        elif key in KEYS['RIGHT']:
            return 'RIGHT'
        elif key in KEYS['QUIT']:
            return 'QUIT'
        elif key.lower() == 'r':
            return 'RESTART'
        
        return None
    
    def clear_buffer(self):
        """Xóa buffer phím."""
        self.key_buffer.clear()
        
    def has_pending_input(self):
        """Kiểm tra có input đang chờ xử lý không."""
        return len(self.key_buffer) > 0