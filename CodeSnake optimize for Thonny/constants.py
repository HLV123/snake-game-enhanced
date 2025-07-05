# constants.py
"""Các hằng số và cấu hình cho game Snake"""

# Kích thước màn hình
GRID_WIDTH = 30
GRID_HEIGHT = 20
CELL_SIZE = 25

# Màu sắc
COLORS = {
    'background': '#1a1a1a',
    'border': '#ffffff',
    'snake_head': '#00ff41',
    'snake_body': '#00cc33',
    'snake_outline': '#004d12',
    'normal_food': '#ff4444',
    'special_food': '#ffd700',
    'text': '#ffffff',
    'ui_bg': '#2d2d2d',
    'button_bg': '#4a4a4a',
    'button_active': '#5a5a5a'
}

# Tốc độ game (milliseconds)
SPEED_SETTINGS = {
    'Slow': 200,
    'Medium': 150,
    'Fast': 100,
    'Very Fast': 50
}

# Điểm số
SCORES = {
    'normal_food': 10,
    'special_food': 50
}

# Game settings
SPECIAL_FOOD_INTERVAL = 5  # Xuất hiện đồ đặc biệt sau mỗi 5 lần ăn bình thường
SPECIAL_FOOD_DURATION = 10000  # Thời gian hiển thị đồ đặc biệt (ms)

# Phím điều khiển
KEYS = {
    'UP': ['Up', 'w', 'W'],
    'DOWN': ['Down', 's', 'S'],
    'LEFT': ['Left', 'a', 'A'],
    'RIGHT': ['Right', 'd', 'D'],
    'PAUSE': ['Shift_L', 'Shift_R'],
    'QUIT': ['q', 'Q', 'Escape']
}