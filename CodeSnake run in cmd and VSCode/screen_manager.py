# screen_manager.py

import curses

class ScreenManager:
    """Quản lý màn hình console bằng curses."""
    def __init__(self):
        self.screen = curses.initscr()
        curses.curs_set(0)
        self.height, self.width = self.screen.getmaxyx()
        self.screen.keypad(True)
        self.screen.timeout(100) # Tốc độ game
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)


    def get_input(self):
        """Nhận phím bấm từ người dùng."""
        return self.screen.getch()

    def clear(self):
        """Xóa màn hình."""
        self.screen.clear()

    def draw_border(self):
        """Vẽ đường viền cho khu vực chơi."""
        self.screen.border(0)

    def draw(self, drawable_object):
        """Vẽ một đối tượng có thể vẽ được."""
        drawable_object.draw(self.screen)
        
    def show_game_over(self, score):
        """Hiển thị thông báo kết thúc game và điểm số."""
        game_over_text = "GAME OVER"
        score_text = f"Score: {score}"
        self.screen.addstr(self.height // 2 - 1, (self.width - len(game_over_text)) // 2, game_over_text)
        self.screen.addstr(self.height // 2, (self.width - len(score_text)) // 2, score_text)
        self.screen.refresh()
        self.screen.timeout(-1) # Chờ người dùng bấm phím để thoát
        self.screen.getch()

    def refresh(self):
        """Cập nhật màn hình."""
        self.screen.refresh()

    def close(self):
        """Đóng curses."""
        curses.endwin()