# main.py - Optimized for Thonny
"""Game loop chính cho Snake Game Enhanced - Tối ưu cho Thonny"""

import time
import sys
import tkinter as tk
from snake import Snake
from food_manager import FoodManager
from ui_manager import UIManager
from input_manager import InputManager
from game_state import GameState
from constants import GRID_WIDTH, GRID_HEIGHT

class SnakeGame:
    """Lớp chính quản lý toàn bộ game."""
    
    def __init__(self):
        self.running = True
        self.ui_manager = None
        self.input_manager = None
        self.game_state = None
        self.snake = None
        self.food_manager = None
        self.last_frame_time = 0
        
        # Initialize components safely
        try:
            self.ui_manager = UIManager()
            self.input_manager = InputManager()
            self.game_state = GameState()
            
            # Bind events
            self.ui_manager.bind_key_events(self.input_manager.handle_key_event)
            
        except Exception as e:
            print(f"Failed to initialize game components: {e}")
            self.running = False
        
    def initialize_game_objects(self):
        """Khởi tạo các đối tượng game."""
        try:
            start_x = GRID_WIDTH // 4
            start_y = GRID_HEIGHT // 2
            
            self.snake = Snake(start_x, start_y, self.game_state.wall_mode)
            self.food_manager = FoodManager()
            return True
        except Exception as e:
            print(f"Failed to initialize game objects: {e}")
            return False

    def show_start_menu(self):
        """Hiển thị menu khởi động."""
        try:
            settings = self.ui_manager.show_start_menu()
            if not settings:  # User closed dialog
                return False
                
            # Apply settings
            self.game_state.start_game(settings['wall_mode'], settings['speed'])
            self.ui_manager.update_speed(settings['speed'])
            self.ui_manager.update_mode(settings['wall_mode'])
            
            return True
        except Exception as e:
            print(f"Error in start menu: {e}")
            return False
    
    def handle_input(self):
        """Xử lý input từ người chơi."""
        try:
            action = self.input_manager.get_next_action()
            
            if action == 'QUIT':
                return False
            elif action == 'PAUSE':
                self.game_state.pause_game()
                self.ui_manager.update_status(self.game_state.get_status_text())
            elif action == 'RESTART' and self.game_state.is_game_over:
                self.restart_game()
            elif action in ['UP', 'DOWN', 'LEFT', 'RIGHT'] and not self.game_state.is_paused:
                if self.snake:
                    self.snake.set_direction(action)
                
            return True
        except Exception as e:
            print(f"Error handling input: {e}")
            return True  # Continue game even if input fails
    
    def update_game_logic(self):
        """Cập nhật logic game."""
        try:
            if not self.game_state.should_update():
                return
                
            if not self.snake or not self.food_manager:
                return
                
            # Di chuyển rắn
            self.snake.move()
            
            # Kiểm tra va chạm
            self.snake.check_collision()
            if not self.snake.is_alive:
                self.game_state.end_game()
                self.ui_manager.update_status(self.game_state.get_status_text())
                return
            
            # Kiểm tra ăn đồ ăn
            snake_head_pos = self.snake.get_head_position()
            current_time = time.time() * 1000
            
            # Kiểm tra đồ ăn thường
            normal_food_result = self.food_manager.check_normal_food_collision(snake_head_pos)
            if normal_food_result:
                # Rắn ăn đồ ăn thường
                self.snake.grow()
                score_gained = self.food_manager.get_score_for_food_type(normal_food_result)
                self.game_state.add_score(score_gained)
                self.game_state.add_food_eaten(normal_food_result)
                
                # Tạo đồ ăn thường mới
                self.food_manager.spawn_normal_food(self.snake.get_body_positions())
                
                # Kiểm tra có cần tạo đồ ăn đặc biệt không
                if normal_food_result == 'normal_food_special_trigger':
                    self.food_manager.spawn_special_food(self.snake.get_body_positions())
            
            # Kiểm tra đồ ăn đặc biệt
            special_food_result = self.food_manager.check_special_food_collision(snake_head_pos)
            if special_food_result:
                # Rắn ăn đồ ăn đặc biệt
                self.snake.grow(2)  # Tăng 2 đoạn cho đồ ăn đặc biệt
                score_gained = self.food_manager.get_score_for_food_type(special_food_result)
                self.game_state.add_score(score_gained)
                self.game_state.add_food_eaten(special_food_result)
            
            # Cập nhật food manager
            self.food_manager.update(current_time)
            
            # Cập nhật UI
            self.ui_manager.update_score(self.game_state.score)
            
        except Exception as e:
            print(f"Error in game logic: {e}")
    
    def render_game(self):
        """Vẽ game lên màn hình."""
        try:
            # Kiểm tra canvas còn khả dụng không
            if not self.ui_manager.clear_canvas():
                return False
            
            # Vẽ border
            if not self.ui_manager.draw_border():
                return False
            
            # Vẽ rắn
            if self.snake:
                self.snake.draw(self.ui_manager.canvas)
            
            # Vẽ đồ ăn
            if self.food_manager:
                self.food_manager.draw(self.ui_manager.canvas)
            
            # Vẽ overlay nếu cần
            if self.game_state.is_paused:
                self.ui_manager.draw_pause_overlay()
            elif self.game_state.is_game_over:
                self.ui_manager.show_game_over(self.game_state.score, self.game_state.high_score)
            
            return True
        except Exception as e:
            print(f"Error rendering: {e}")
            return False
    
    def restart_game(self):
        """Restart game."""
        try:
            self.game_state.restart_game()
            if self.initialize_game_objects():
                self.input_manager.clear_buffer()
                self.ui_manager.remove_game_over()
                self.ui_manager.update_status(self.game_state.get_status_text())
                self.ui_manager.update_score(self.game_state.score)
        except Exception as e:
            print(f"Error restarting game: {e}")
    
    def run(self):
        """Chạy game loop chính - Tối ưu cho Thonny."""
        try:
            print("🐍 Starting Snake Game Enhanced...")
            
            # Hiển thị menu khởi động
            if not self.show_start_menu():
                print("Game cancelled by user")
                return
            
            # Khởi tạo game objects
            if not self.initialize_game_objects():
                print("Failed to initialize game objects")
                return
                
            self.ui_manager.update_status(self.game_state.get_status_text())
            
            # Game loop chính với tối ưu cho Thonny
            frame_count = 0
            while self.running:
                try:
                    # Kiểm tra window còn tồn tại không
                    if not self.ui_manager.refresh():
                        print("Window closed")
                        break
                    
                    # Xử lý input
                    if not self.handle_input():
                        print("User quit")
                        break
                    
                    # Cập nhật game logic
                    if self.game_state and self.game_state.is_running:
                        self.update_game_logic()
                    
                    # Render với frame limiting
                    current_time = time.time()
                    if current_time - self.last_frame_time >= 0.016:  # ~60 FPS
                        if not self.render_game():
                            print("Render failed")
                            break
                        self.last_frame_time = current_time
                    
                    # Throttle để tránh overload CPU
                    time.sleep(0.001)  # 1ms sleep để giải phóng CPU
                    
                    # Periodic cleanup cho Thonny
                    frame_count += 1
                    if frame_count % 1000 == 0:  # Mỗi ~16 giây
                        try:
                            # Force garbage collection
                            import gc
                            gc.collect()
                        except:
                            pass
                    
                except KeyboardInterrupt:
                    print("\nGame interrupted by Ctrl+C")
                    break
                except tk.TclError as e:
                    print(f"Tkinter error: {e}")
                    break
                except Exception as e:
                    print(f"Unexpected error in game loop: {e}")
                    # Try to continue for minor errors
                    time.sleep(0.1)
                    continue
                    
        except Exception as e:
            print(f"Fatal game error: {e}")
            import traceback
            traceback.print_exc()
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Dọn dẹp resources - Quan trọng cho Thonny."""
        try:
            print("🧹 Cleaning up...")
            self.running = False
            
            if self.ui_manager:
                self.ui_manager.close()
            
            # Force cleanup
            self.snake = None
            self.food_manager = None
            self.game_state = None
            self.input_manager = None
            
            print("🐍 Thanks for playing Snake Game Enhanced!")
            if self.game_state:
                stats = self.game_state.get_statistics()
                print(f"📊 Final Statistics:")
                print(f"   Score: {stats['score']}")
                print(f"   High Score: {stats['high_score']}")
                print(f"   Normal Food Eaten: {stats['normal_food_eaten']}")
                print(f"   Special Food Eaten: {stats['special_food_eaten']}")
                print(f"   Game Time: {stats['game_time']:.1f} seconds")
        except Exception as e:
            print(f"Error during cleanup: {e}")

def main():
    """Entry point của game - Tối ưu cho Thonny."""
    
    # Kiểm tra môi trường Thonny
    try:
        import thonny
        print("🔧 Running in Thonny environment")
    except ImportError:
        print("🔧 Running in standard Python environment")
    
    try:
        game = SnakeGame()
        if game.running:
            game.run()
        else:
            print("❌ Failed to initialize game")
            return 1
    except KeyboardInterrupt:
        print("\n🛑 Game stopped by user")
        return 0
    except Exception as e:
        print(f"❌ Failed to start game: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    # Đảm bảo thoát sạch cho Thonny
    try:
        exit_code = main()
        sys.exit(exit_code)
    except SystemExit:
        pass  # Normal exit
    except Exception as e:
        print(f"💥 Critical error: {e}")
        sys.exit(1)