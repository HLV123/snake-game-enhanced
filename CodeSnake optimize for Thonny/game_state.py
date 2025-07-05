# game_state.py
"""Quản lý trạng thái game và logic chính"""

import time
import json
import os
from constants import SPEED_SETTINGS, GRID_WIDTH, GRID_HEIGHT

class GameState:
    """Quản lý trạng thái và logic chính của game."""
    
    def __init__(self):
        self.score = 0
        self.high_score = self.load_high_score()
        self.speed_name = "Medium"
        self.speed_delay = SPEED_SETTINGS[self.speed_name]
        self.wall_mode = True
        self.is_paused = False
        self.is_game_over = False
        self.is_running = False
        self.last_update_time = 0
        
        # Statistics
        self.normal_food_eaten = 0
        self.special_food_eaten = 0
        self.game_start_time = 0
        
    def start_game(self, wall_mode, speed_name):
        """Bắt đầu game mới với cài đặt."""
        self.wall_mode = wall_mode
        self.speed_name = speed_name
        self.speed_delay = SPEED_SETTINGS[speed_name]
        self.score = 0
        self.is_paused = False
        self.is_game_over = False
        self.is_running = True
        self.last_update_time = time.time() * 1000
        self.game_start_time = time.time()
        
        # Reset statistics
        self.normal_food_eaten = 0
        self.special_food_eaten = 0
        
    def pause_game(self):
        """Tạm dừng/tiếp tục game."""
        if not self.is_game_over:
            self.is_paused = not self.is_paused
            if not self.is_paused:
                # Reset timer khi resume
                self.last_update_time = time.time() * 1000
    
    def end_game(self):
        """Kết thúc game."""
        self.is_game_over = True
        self.is_running = False
        
        # Update high score
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
    
    def restart_game(self):
        """Restart game với cài đặt hiện tại."""
        self.start_game(self.wall_mode, self.speed_name)
    
    def should_update(self):
        """Kiểm tra có nên update game logic không."""
        if self.is_paused or self.is_game_over:
            return False
            
        current_time = time.time() * 1000
        if current_time - self.last_update_time >= self.speed_delay:
            self.last_update_time = current_time
            return True
        return False
    
    def add_score(self, points):
        """Thêm điểm."""
        self.score += points
        
    def add_food_eaten(self, food_type):
        """Cập nhật thống kê đồ ăn."""
        if food_type in ['normal_food', 'normal_food_special_trigger']:
            self.normal_food_eaten += 1
        elif food_type == 'special_food':
            self.special_food_eaten += 1
    
    def get_status_text(self):
        """Lấy text trạng thái hiện tại."""
        if self.is_game_over:
            return "Game Over"
        elif self.is_paused:
            return "Paused"
        elif self.is_running:
            return "Playing"
        else:
            return "Ready"
    
    def get_game_time(self):
        """Lấy thời gian chơi (seconds)."""
        if self.game_start_time:
            return time.time() - self.game_start_time
        return 0
    
    def load_high_score(self):
        """Load high score từ file."""
        try:
            if os.path.exists('snake_highscore.json'):
                with open('snake_highscore.json', 'r') as f:
                    data = json.load(f)
                    return data.get('high_score', 0)
        except:
            pass
        return 0
    
    def save_high_score(self):
        """Lưu high score vào file."""
        try:
            data = {
                'high_score': self.high_score,
                'last_updated': time.time()
            }
            with open('snake_highscore.json', 'w') as f:
                json.dump(data, f)
        except:
            pass  # Bỏ qua lỗi lưu file
    
    def get_statistics(self):
        """Lấy thống kê game."""
        return {
            'score': self.score,
            'high_score': self.high_score,
            'normal_food_eaten': self.normal_food_eaten,
            'special_food_eaten': self.special_food_eaten,
            'game_time': self.get_game_time(),
            'speed': self.speed_name,
            'mode': 'Wall Mode' if self.wall_mode else 'Wrap Mode'
        }