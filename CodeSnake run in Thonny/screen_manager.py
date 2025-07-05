# screen_manager.py

import tkinter as tk
from tkinter import messagebox

class ScreenManager:
    """Quản lý màn hình game bằng tkinter."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake Game")
        self.root.resizable(False, False)
        
        # Cài đặt kích thước
        self.cell_size = 20
        self.width = 30  # số ô ngang
        self.height = 20  # số ô dọc
        
        # Tạo canvas
        self.canvas = tk.Canvas(
            self.root,
            width=self.width * self.cell_size,
            height=self.height * self.cell_size,
            bg='black',
            highlightthickness=0
        )
        self.canvas.pack()
        
        # Label hiển thị điểm
        self.score_label = tk.Label(
            self.root, 
            text="Score: 0", 
            font=("Arial", 14),
            bg='black',
            fg='white'
        )
        self.score_label.pack()
        
        # Hướng dẫn
        self.instruction_label = tk.Label(
            self.root,
            text="Dùng phím mũi tên để điều khiển, 'Q' để thoát",
            font=("Arial", 10),
            bg='black',
            fg='gray'
        )
        self.instruction_label.pack()
        
        # Biến lưu phím bấm
        self.last_key = None
        
        # Bind sự kiện phím
        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.focus_set()
        
        # Đặt màu nền cho root
        self.root.configure(bg='black')

    def on_key_press(self, event):
        """Xử lý sự kiện bấm phím."""
        self.last_key = event.keysym

    def get_input(self):
        """Nhận phím bấm từ người dùng."""
        key = self.last_key
        self.last_key = None  # Reset sau khi đọc
        
        # Chuyển đổi tên phím tkinter sang format tương thích
        if key == 'Up':
            return 'KEY_UP'
        elif key == 'Down':
            return 'KEY_DOWN'
        elif key == 'Left':
            return 'KEY_LEFT'
        elif key == 'Right':
            return 'KEY_RIGHT'
        elif key and key.lower() == 'q':
            return 'q'
        else:
            return None

    def clear(self):
        """Xóa canvas."""
        self.canvas.delete("all")

    def draw_border(self):
        """Vẽ đường viền cho khu vực chơi."""
        # Vẽ viền ngoài
        self.canvas.create_rectangle(
            0, 0, 
            self.width * self.cell_size, 
            self.height * self.cell_size,
            outline='white',
            width=2
        )

    def draw(self, drawable_object):
        """Vẽ một đối tượng có thể vẽ được."""
        drawable_object.draw(self.canvas, self.cell_size)
        
    def update_score(self, score):
        """Cập nhật điểm số."""
        self.score_label.config(text=f"Score: {score}")
        
    def show_game_over(self, score):
        """Hiển thị thông báo kết thúc game và điểm số."""
        # Vẽ overlay game over lên canvas
        canvas_width = self.width * self.cell_size
        canvas_height = self.height * self.cell_size
        
        # Tạo hình chữ nhật mờ
        self.canvas.create_rectangle(
            0, 0, canvas_width, canvas_height,
            fill='black', stipple='gray50', outline=''
        )
        
        # Text game over
        self.canvas.create_text(
            canvas_width // 2,
            canvas_height // 2 - 20,
            text="GAME OVER",
            fill='red',
            font=("Arial", 24, "bold")
        )
        
        # Text điểm số
        self.canvas.create_text(
            canvas_width // 2,
            canvas_height // 2 + 10,
            text=f"Final Score: {score}",
            fill='white',
            font=("Arial", 16)
        )
        
        # Text hướng dẫn
        self.canvas.create_text(
            canvas_width // 2,
            canvas_height // 2 + 40,
            text="Press 'R' to restart or close window to exit",
            fill='yellow',
            font=("Arial", 12)
        )
        
        self.refresh()

    def refresh(self):
        """Cập nhật màn hình."""
        self.root.update()
        
    def process_events(self):
        """Xử lý các sự kiện tkinter."""
        try:
            self.root.update_idletasks()
            self.root.update()
        except tk.TclError:
            # Cửa sổ đã bị đóng
            return False
        return True

    def close(self):
        """Đóng cửa sổ."""
        try:
            self.root.destroy()
        except:
            pass