# food_manager.py
"""Quản lý hệ thống đồ ăn bao gồm đồ ăn thường và đặc biệt"""

import random
import time
from game_object import GameObject
from constants import GRID_WIDTH, GRID_HEIGHT, SPECIAL_FOOD_INTERVAL, SPECIAL_FOOD_DURATION, SCORES

class FoodManager:
    """Quản lý tất cả các loại đồ ăn trong game."""
    
    def __init__(self):
        self.normal_food = None
        self.special_food = None
        self.normal_food_eaten = 0  # Đếm số đồ ăn thường đã ăn
        self.special_food_spawn_time = 0  # Thời gian spawn đồ ăn đặc biệt
        self.special_food_active = False
        
        # Tạo đồ ăn thường đầu tiên
        self.spawn_normal_food([])

    def spawn_normal_food(self, snake_body_positions):
        """Tạo đồ ăn thường ở vị trí ngẫu nhiên."""
        occupied_positions = set(snake_body_positions)
        
        # Thêm vị trí đồ ăn đặc biệt nếu có
        if self.special_food and self.special_food_active:
            occupied_positions.add(self.special_food.get_position())
        
        # Tìm vị trí trống
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in occupied_positions:
                self.normal_food = GameObject(x, y, 'normal_food')
                break

    def spawn_special_food(self, snake_body_positions):
        """Tạo đồ ăn đặc biệt."""
        if self.special_food_active:
            return  # Đã có đồ ăn đặc biệt
            
        occupied_positions = set(snake_body_positions)
        occupied_positions.add(self.normal_food.get_position())
        
        # Tìm vị trí trống
        attempts = 0
        while attempts < 100:  # Tránh vòng lặp vô hạn
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in occupied_positions:
                self.special_food = GameObject(x, y, 'special_food')
                self.special_food_spawn_time = time.time() * 1000  # Convert to milliseconds
                self.special_food_active = True
                break
            attempts += 1

    def update(self, current_time):
        """Cập nhật trạng thái đồ ăn đặc biệt."""
        if (self.special_food_active and 
            current_time - self.special_food_spawn_time > SPECIAL_FOOD_DURATION):
            # Đồ ăn đặc biệt hết hạn
            self.special_food_active = False
            self.special_food = None

    def check_normal_food_collision(self, snake_head_pos):
        """Kiểm tra va chạm với đồ ăn thường."""
        if self.normal_food and snake_head_pos == self.normal_food.get_position():
            self.normal_food_eaten += 1
            
            # Kiểm tra có nên spawn đồ ăn đặc biệt không
            if self.normal_food_eaten % SPECIAL_FOOD_INTERVAL == 0:
                return 'normal_food_special_trigger'
            
            return 'normal_food'
        return None

    def check_special_food_collision(self, snake_head_pos):
        """Kiểm tra va chạm với đồ ăn đặc biệt."""
        if (self.special_food_active and self.special_food and 
            snake_head_pos == self.special_food.get_position()):
            self.special_food_active = False
            self.special_food = None
            return 'special_food'
        return None

    def get_score_for_food_type(self, food_type):
        """Trả về điểm số cho loại đồ ăn."""
        if food_type in ['normal_food', 'normal_food_special_trigger']:
            return SCORES['normal_food']
        elif food_type == 'special_food':
            return SCORES['special_food']
        return 0

    def draw(self, canvas):
        """Vẽ tất cả đồ ăn lên canvas."""
        if self.normal_food:
            self.normal_food.draw(canvas)
            
        if self.special_food_active and self.special_food:
            self.special_food.draw(canvas)

    def get_food_positions(self):
        """Trả về vị trí của tất cả đồ ăn hiện tại."""
        positions = []
        if self.normal_food:
            positions.append(self.normal_food.get_position())
        if self.special_food_active and self.special_food:
            positions.append(self.special_food.get_position())
        return positions

    def reset(self):
        """Reset food manager về trạng thái ban đầu."""
        self.normal_food = None
        self.special_food = None
        self.normal_food_eaten = 0
        self.special_food_spawn_time = 0
        self.special_food_active = False
        self.spawn_normal_food([])