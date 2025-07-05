# main.py

import time
from screen_manager import ScreenManager
from snake import Snake
from food import Food

def main():
    screen_manager = ScreenManager()
    width = screen_manager.width
    height = screen_manager.height

    # Khởi tạo các đối tượng game
    player_snake = Snake(width // 4, height // 2)
    current_food = Food(width, height)
    score = 0
    
    # Cập nhật điểm ban đầu
    screen_manager.update_score(score)
    
    # Biến điều khiển restart
    game_over_handled = False

    # Vòng lặp chính của game
    try:
        while True:
            # Xử lý sự kiện tkinter
            if not screen_manager.process_events():
                break  # Cửa sổ đã đóng
                
            if player_snake.is_alive:
                # 1. Xử lý input
                key = screen_manager.get_input()

                if key == 'KEY_UP':
                    player_snake.set_direction('UP')
                elif key == 'KEY_DOWN':
                    player_snake.set_direction('DOWN')
                elif key == 'KEY_LEFT':
                    player_snake.set_direction('LEFT')
                elif key == 'KEY_RIGHT':
                    player_snake.set_direction('RIGHT')
                elif key == 'q':  # Thoát game
                    break

                # 2. Cập nhật trạng thái game
                player_snake.move()

                # Kiểm tra ăn mồi
                if player_snake.body[0].get_position() == current_food.get_position():
                    player_snake.grow()
                    current_food.respawn(player_snake.body)
                    score += 10
                    screen_manager.update_score(score)
                    
                # Kiểm tra va chạm
                player_snake.check_collision(width, height)

                # 3. Vẽ lại mọi thứ
                screen_manager.clear()
                screen_manager.draw_border()
                screen_manager.draw(player_snake)
                screen_manager.draw(current_food)
                screen_manager.refresh()
                
                # Tạm dừng để kiểm soát tốc độ game
                time.sleep(0.15)
                
            else:
                # Game Over - chỉ hiển thị một lần
                if not game_over_handled:
                    screen_manager.show_game_over(score)
                    game_over_handled = True
                
                # Kiểm tra phím restart
                key = screen_manager.get_input()
                if key and key.lower() == 'r':
                    # Restart game
                    player_snake = Snake(width // 4, height // 2)
                    current_food = Food(width, height)
                    score = 0
                    screen_manager.update_score(score)
                    game_over_handled = False
                elif key == 'q':
                    break
                    
                # Xử lý sự kiện để tránh đóng băng
                time.sleep(0.1)
                    
    except Exception as e:
        print(f"Lỗi trong game: {e}")
    finally:
        # Đóng cửa sổ
        screen_manager.close()
        print("Game đã kết thúc.")

if __name__ == "__main__":
    main()