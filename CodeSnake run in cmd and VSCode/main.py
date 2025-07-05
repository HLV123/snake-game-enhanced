# main.py

import curses
from screen_manager import ScreenManager
from snake import Snake
from food import Food

def main(stdscr):
    screen_manager = ScreenManager()
    width = screen_manager.width
    height = screen_manager.height

    # Khởi tạo các đối tượng game
    player_snake = Snake(width // 4, height // 2)
    current_food = Food(width, height)
    score = 0

    # Vòng lặp chính của game
    while player_snake.is_alive:
        # 1. Xử lý input
        key = screen_manager.get_input()

        if key == curses.KEY_UP:
            player_snake.set_direction('UP')
        elif key == curses.KEY_DOWN:
            player_snake.set_direction('DOWN')
        elif key == curses.KEY_LEFT:
            player_snake.set_direction('LEFT')
        elif key == curses.KEY_RIGHT:
            player_snake.set_direction('RIGHT')
        elif key == ord('q'): # Thoát game
            break

        # 2. Cập nhật trạng thái game
        player_snake.move()

        # Kiểm tra ăn mồi
        if player_snake.body[0].get_position() == current_food.get_position():
            player_snake.grow()
            current_food.respawn(player_snake.body)
            score += 10
            
        # Kiểm tra va chạm
        player_snake.check_collision(width, height)


        # 3. Vẽ lại mọi thứ
        screen_manager.clear()
        screen_manager.draw_border()
        screen_manager.draw(player_snake)
        screen_manager.draw(current_food)
        screen_manager.screen.addstr(0, 2, f'Score: {score}') # Hiển thị điểm
        screen_manager.refresh()
        
    # Game Over
    screen_manager.show_game_over(score)


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except curses.error as e:
        print(f"Lỗi curses: {e}")
    finally:
        # Đảm bảo curses được đóng đúng cách
        curses.endwin()
        print("Game đã kết thúc.")