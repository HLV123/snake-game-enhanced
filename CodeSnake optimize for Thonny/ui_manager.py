# ui_manager.py
"""Quản lý giao diện người dùng và các màn hình menu"""

import tkinter as tk
from tkinter import ttk, messagebox
from constants import COLORS, SPEED_SETTINGS, GRID_WIDTH, GRID_HEIGHT, CELL_SIZE

class UIManager:
    """Quản lý tất cả giao diện người dùng."""
    
    def __init__(self):
        self.root = None
        self.canvas = None
        self.info_frame = None
        self.score_label = None
        self.speed_label = None
        self.mode_label = None
        self.status_label = None
        self.setup_ui()

    def setup_ui(self):
        """Thiết lập giao diện chính."""
        self.root = tk.Tk()
        self.root.title("🐍 Snake Game Enhanced")
        self.root.resizable(False, False)
        self.root.configure(bg=COLORS['ui_bg'])
        
        # Thiết lập icon và style
        self.setup_styles()
        
        # Tạo main frame
        main_frame = tk.Frame(self.root, bg=COLORS['ui_bg'])
        main_frame.pack(padx=10, pady=10)
        
        # Tạo info frame (thông tin game)
        self.create_info_frame(main_frame)
        
        # Tạo canvas game
        self.create_game_canvas(main_frame)
        
        # Tạo control frame (hướng dẫn)
        self.create_control_frame(main_frame)
        
        # Bind events
        self.root.focus_set()
        
    def setup_styles(self):
        """Thiết lập styles cho UI."""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure styles
        style.configure('Game.TLabel', 
                       background=COLORS['ui_bg'], 
                       foreground=COLORS['text'],
                       font=('Arial', 11, 'bold'))
        
        style.configure('Title.TLabel',
                       background=COLORS['ui_bg'],
                       foreground=COLORS['special_food'],
                       font=('Arial', 14, 'bold'))

    def create_info_frame(self, parent):
        """Tạo frame hiển thị thông tin game."""
        self.info_frame = tk.Frame(parent, bg=COLORS['ui_bg'])
        self.info_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Title
        title_label = ttk.Label(self.info_frame, text="🐍 SNAKE GAME ENHANCED", 
                               style='Title.TLabel')
        title_label.pack()
        
        # Info grid
        info_grid = tk.Frame(self.info_frame, bg=COLORS['ui_bg'])
        info_grid.pack(fill=tk.X, pady=5)
        
        # Score
        score_frame = tk.Frame(info_grid, bg=COLORS['button_bg'], relief=tk.RAISED, bd=1)
        score_frame.pack(side=tk.LEFT, padx=5, pady=2, fill=tk.X, expand=True)
        self.score_label = ttk.Label(score_frame, text="Score: 0", style='Game.TLabel')
        self.score_label.pack(pady=5)
        
        # Speed
        speed_frame = tk.Frame(info_grid, bg=COLORS['button_bg'], relief=tk.RAISED, bd=1)
        speed_frame.pack(side=tk.LEFT, padx=5, pady=2, fill=tk.X, expand=True)
        self.speed_label = ttk.Label(speed_frame, text="Speed: Medium", style='Game.TLabel')
        self.speed_label.pack(pady=5)
        
        # Mode
        mode_frame = tk.Frame(info_grid, bg=COLORS['button_bg'], relief=tk.RAISED, bd=1)
        mode_frame.pack(side=tk.LEFT, padx=5, pady=2, fill=tk.X, expand=True)
        self.mode_label = ttk.Label(mode_frame, text="Mode: Wall Mode", style='Game.TLabel')
        self.mode_label.pack(pady=5)
        
        # Status
        status_frame = tk.Frame(info_grid, bg=COLORS['button_bg'], relief=tk.RAISED, bd=1)
        status_frame.pack(side=tk.LEFT, padx=5, pady=2, fill=tk.X, expand=True)
        self.status_label = ttk.Label(status_frame, text="Status: Ready", style='Game.TLabel')
        self.status_label.pack(pady=5)

    def create_game_canvas(self, parent):
        """Tạo canvas chính cho game."""
        canvas_frame = tk.Frame(parent, bg=COLORS['border'], relief=tk.SOLID, bd=2)
        canvas_frame.pack(pady=5)
        
        self.canvas = tk.Canvas(
            canvas_frame,
            width=GRID_WIDTH * CELL_SIZE,
            height=GRID_HEIGHT * CELL_SIZE,
            bg=COLORS['background'],
            highlightthickness=0
        )
        self.canvas.pack()

    def create_control_frame(self, parent):
        """Tạo frame hướng dẫn điều khiển."""
        control_frame = tk.Frame(parent, bg=COLORS['ui_bg'])
        control_frame.pack(fill=tk.X, pady=(5, 0))
        
        # Controls info
        controls_text = (
            "🎮 Controls: Arrow Keys/WASD to move | "
            "Shift to Pause/Resume | Q/Esc to Quit | "
            "🌟 Collect golden stars for bonus points!"
        )
        
        control_label = tk.Label(
            control_frame,
            text=controls_text,
            bg=COLORS['ui_bg'],
            fg=COLORS['text'],
            font=('Arial', 9),
            wraplength=GRID_WIDTH * CELL_SIZE
        )
        control_label.pack()

    def show_start_menu(self):
        """Hiển thị menu khởi động và trả về cài đặt được chọn."""
        settings = {}
        
        # Tạo dialog window
        dialog = tk.Toplevel(self.root)
        dialog.title("Game Settings")
        dialog.geometry("500x450")
        dialog.configure(bg=COLORS['ui_bg'])
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center dialog
        dialog.geometry("+%d+%d" % (
            self.root.winfo_rootx() + 50,
            self.root.winfo_rooty() + 50
        ))
        
        # Title
        title_label = tk.Label(
            dialog, 
            text="🐍 Snake Game Settings",
            font=('Arial', 16, 'bold'),
            bg=COLORS['ui_bg'],
            fg=COLORS['special_food']
        )
        title_label.pack(pady=20)
        
        # Wall Mode Selection
        wall_frame = tk.LabelFrame(
            dialog, 
            text="Wall Mode", 
            bg=COLORS['ui_bg'], 
            fg=COLORS['text'],
            font=('Arial', 11, 'bold')
        )
        wall_frame.pack(pady=10, padx=20, fill=tk.X)
        
        wall_mode = tk.StringVar(value="wall")
        
        tk.Radiobutton(
            wall_frame,
            text="🚧 Wall Mode (Die when hit wall)",
            variable=wall_mode,
            value="wall",
            bg=COLORS['ui_bg'],
            fg=COLORS['text'],
            selectcolor=COLORS['button_bg'],
            font=('Arial', 10)
        ).pack(anchor=tk.W, pady=5)
        
        tk.Radiobutton(
            wall_frame,
            text="🌀 Wrap Mode (Pass through walls)",
            variable=wall_mode,
            value="wrap",
            bg=COLORS['ui_bg'],
            fg=COLORS['text'],
            selectcolor=COLORS['button_bg'],
            font=('Arial', 10)
        ).pack(anchor=tk.W, pady=5)
        
        # Speed Selection
        speed_frame = tk.LabelFrame(
            dialog, 
            text="Game Speed", 
            bg=COLORS['ui_bg'], 
            fg=COLORS['text'],
            font=('Arial', 11, 'bold')
        )
        speed_frame.pack(pady=10, padx=20, fill=tk.X)
        
        speed_var = tk.StringVar(value="Medium")
        
        for speed_name in SPEED_SETTINGS.keys():
            tk.Radiobutton(
                speed_frame,
                text=f"🚀 {speed_name}",
                variable=speed_var,
                value=speed_name,
                bg=COLORS['ui_bg'],
                fg=COLORS['text'],
                selectcolor=COLORS['button_bg'],
                font=('Arial', 10)
            ).pack(anchor=tk.W, pady=2)
        
        # Buttons
        button_frame = tk.Frame(dialog, bg=COLORS['ui_bg'])
        button_frame.pack(pady=20)
        
        def start_game():
            settings['wall_mode'] = wall_mode.get() == "wall"
            settings['speed'] = speed_var.get()
            dialog.destroy()
        
        def show_instructions():
            instructions = """
🐍 SNAKE GAME ENHANCED - Instructions

🎯 Goal: Eat food to grow and score points!

🍎 Normal Food (Red circles): +10 points
⭐ Special Food (Golden stars): +50 points
   • Appears every 5 normal foods eaten
   • Disappears after 10 seconds

🎮 Controls:
   • Arrow Keys or WASD: Move snake
   • Shift: Pause/Resume game
   • Q or Escape: Quit game

🏆 Game Modes:
   • Wall Mode: Game over when hitting walls
   • Wrap Mode: Snake wraps around screen edges

💡 Tips:
   • Plan your path to special food
   • Use pause to think in tricky situations
   • Special food gives 5x normal points!
            """
            messagebox.showinfo("Instructions", instructions)
        
        tk.Button(
            button_frame,
            text="📖 Instructions",
            command=show_instructions,
            bg=COLORS['button_bg'],
            fg=COLORS['text'],
            font=('Arial', 11),
            padx=20,
            pady=5
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            button_frame,
            text="🎮 Start Game",
            command=start_game,
            bg=COLORS['special_food'],
            fg='black',
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=5
        ).pack(side=tk.LEFT, padx=10)
        
        # Wait for dialog to close
        self.root.wait_window(dialog)
        return settings

    def update_score(self, score):
        """Cập nhật hiển thị điểm số."""
        if self.score_label:
            self.score_label.config(text=f"Score: {score}")

    def update_speed(self, speed_name):
        """Cập nhật hiển thị tốc độ."""
        if self.speed_label:
            self.speed_label.config(text=f"Speed: {speed_name}")

    def update_mode(self, is_wall_mode):
        """Cập nhật hiển thị chế độ."""
        if self.mode_label:
            mode_text = "Wall Mode" if is_wall_mode else "Wrap Mode"
            self.mode_label.config(text=f"Mode: {mode_text}")

    def update_status(self, status):
        """Cập nhật trạng thái game."""
        if self.status_label:
            color_map = {
                'Ready': COLORS['text'],
                'Playing': COLORS['snake_head'],
                'Paused': COLORS['special_food'],
                'Game Over': COLORS['normal_food']
            }
            self.status_label.config(
                text=f"Status: {status}",
                foreground=color_map.get(status, COLORS['text'])
            )

    def draw_border(self):
        """Vẽ đường viền cho game area."""
        if self.canvas:
            try:
                self.canvas.create_rectangle(
                    0, 0,
                    GRID_WIDTH * CELL_SIZE - 1,
                    GRID_HEIGHT * CELL_SIZE - 1,
                    outline=COLORS['border'],
                    width=1
                )
                return True
            except tk.TclError:
                return False
        return False

    def clear_canvas(self):
        """Xóa canvas."""
        if self.canvas:
            try:
                self.canvas.delete("all")
            except tk.TclError:
                # Canvas đã bị destroy
                return False
        return True

    def draw_pause_overlay(self):
        """Vẽ overlay khi game bị pause."""
        if not self.canvas:
            return False
            
        try:
            canvas_width = GRID_WIDTH * CELL_SIZE
            canvas_height = GRID_HEIGHT * CELL_SIZE
            
            # Semi-transparent overlay
            self.canvas.create_rectangle(
                0, 0, canvas_width, canvas_height,
                fill='black', stipple='gray50', outline='', tags='pause_overlay'
            )
            
            # Pause text
            self.canvas.create_text(
                canvas_width // 2, canvas_height // 2 - 20,
                text="⏸️ PAUSED",
                fill=COLORS['special_food'],
                font=('Arial', 24, 'bold'),
                tags='pause_overlay'
            )
            
            self.canvas.create_text(
                canvas_width // 2, canvas_height // 2 + 20,
                text="Press Shift to resume",
                fill=COLORS['text'],
                font=('Arial', 14),
                tags='pause_overlay'
            )
            return True
        except tk.TclError:
            return False

    def remove_pause_overlay(self):
        """Xóa pause overlay."""
        if self.canvas:
            try:
                self.canvas.delete('pause_overlay')
                return True
            except tk.TclError:
                return False
        return False

    def show_game_over(self, score, high_score=None):
        """Hiển thị màn hình game over."""
        if not self.canvas:
            return False
            
        try:
            canvas_width = GRID_WIDTH * CELL_SIZE
            canvas_height = GRID_HEIGHT * CELL_SIZE
            
            # Game over overlay
            self.canvas.create_rectangle(
                0, 0, canvas_width, canvas_height,
                fill='black', stipple='gray25', outline='', tags='game_over'
            )
            
            # Game over text
            self.canvas.create_text(
                canvas_width // 2, canvas_height // 2 - 60,
                text="💀 GAME OVER",
                fill=COLORS['normal_food'],
                font=('Arial', 28, 'bold'),
                tags='game_over'
            )
            
            # Score
            self.canvas.create_text(
                canvas_width // 2, canvas_height // 2 - 20,
                text=f"Final Score: {score}",
                fill=COLORS['text'],
                font=('Arial', 16, 'bold'),
                tags='game_over'
            )
            
            # High score (if provided)
            if high_score is not None:
                if score >= high_score:
                    self.canvas.create_text(
                        canvas_width // 2, canvas_height // 2 + 10,
                        text="🏆 NEW HIGH SCORE! 🏆",
                        fill=COLORS['special_food'],
                        font=('Arial', 14, 'bold'),
                        tags='game_over'
                    )
                else:
                    self.canvas.create_text(
                        canvas_width // 2, canvas_height // 2 + 10,
                        text=f"High Score: {high_score}",
                        fill=COLORS['special_food'],
                        font=('Arial', 12),
                        tags='game_over'
                    )
            
            # Instructions
            self.canvas.create_text(
                canvas_width // 2, canvas_height // 2 + 40,
                text="Press 'R' to restart or 'Q' to quit",
                fill=COLORS['text'],
                font=('Arial', 12),
                tags='game_over'
            )
            return True
        except tk.TclError:
            return False

    def remove_game_over(self):
        """Xóa game over overlay."""
        if self.canvas:
            try:
                self.canvas.delete('game_over')
                return True
            except tk.TclError:
                return False
        return False

    def refresh(self):
        """Cập nhật màn hình."""
        if self.root:
            try:
                self.root.update_idletasks()
                self.root.update()
                return True
            except tk.TclError:
                # Cửa sổ đã bị đóng
                return False
        return False

    def bind_key_events(self, callback):
        """Bind sự kiện bàn phím."""
        if self.root:
            self.root.bind("<KeyPress>", callback)

    def close(self):
        """Đóng UI."""
        if self.root:
            try:
                self.root.destroy()
            except:
                pass