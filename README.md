# 🐍 Snake Game Enhanced

A modern, feature-rich Snake game built with Python and Tkinter, optimized for educational environments like Thonny IDE.

## ✨ Features

### 🎮 Game Modes
- **Wall Mode**: Classic gameplay - game over when hitting walls
- **Wrap Mode**: Snake passes through walls and appears on the opposite side

### 🍎 Food System
- **Normal Food** (🔴): Worth 10 points each
- **Special Food** (⭐): Golden stars worth 50 points
  - Appears every 5 normal foods eaten
  - Disappears after 10 seconds if not collected
  - Makes snake grow by 2 segments instead of 1

### ⚡ Speed Settings
- **Slow**: 200ms delay - Perfect for beginners
- **Medium**: 150ms delay - Balanced gameplay
- **Fast**: 100ms delay - For experienced players
- **Very Fast**: 50ms delay - Challenge mode

### 🎯 Game Features
- **Score System**: Track your current and high scores
- **Statistics**: Detailed game statistics including foods eaten and playtime
- **Pause/Resume**: Press Shift to pause anytime
- **Smooth Controls**: Arrow keys or WASD movement
- **Visual Effects**: Modern UI with gradients and animations
- **High Score Persistence**: Automatically saves your best score

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Tkinter (usually included with Python)

### Installation

**Run the game**
   ```bash
   python main.py
   ```

### For Thonny Users
1. Download all Python files to a folder
2. Open `main.py` in Thonny
3. Press F5 or click the Run button
4. Enjoy the game!

## 🎮 Controls

| Key(s) | Action |
|--------|--------|
| `↑` `↓` `←` `→` | Move snake |
| `W` `A` `S` `D` | Alternative movement |
| `Shift` | Pause/Resume game |
| `Q` / `Esc` | Quit game |
| `R` | Restart (when game over) |

## 📁 Project Structure

```
snake-game-enhanced/
│
├── main.py              # Main game loop and entry point
├── snake.py             # Snake class with movement and collision logic
├── food_manager.py      # Food spawning and management system
├── ui_manager.py        # User interface and rendering
├── input_manager.py     # Keyboard input handling
├── game_state.py        # Game state and scoring system
├── game_object.py       # Base class for all game objects
├── constants.py         # Game configuration and constants
├── README.md           # This file
└── snake_highscore.json # High score storage (created automatically)
```

## 🛠️ Technical Details

### Architecture
- **Object-Oriented Design**: Clean separation of concerns
- **Modular Structure**: Each component in separate files
- **Error Handling**: Robust error handling for stability
- **Resource Management**: Proper cleanup and memory management

### Key Classes
- `SnakeGame`: Main game controller
- `Snake`: Snake entity with movement and collision detection
- `FoodManager`: Handles both normal and special food
- `UIManager`: Manages all UI elements and rendering
- `GameState`: Tracks score, statistics, and game status
- `InputManager`: Handles keyboard input with buffering

### Performance Optimizations
- Frame rate limiting (~60 FPS)
- Efficient collision detection
- Memory management for long gaming sessions
- Optimized for Thonny IDE environment


## 🏆 Scoring System

| Item | Points | Growth | Special Effect |
|------|--------|--------|----------------|
| Normal Food 🔴 | 10 | +1 segment | Triggers special food every 5 eaten |
| Special Food ⭐ | 50 | +2 segments | Limited time (10 seconds) |

## 🐛 Troubleshooting

### Common Issues

**Game window doesn't appear**
- Make sure Tkinter is installed: `python -m tkinter`
- Try running with `python3 main.py` on macOS/Linux

**Controls not responding**
- Click on the game window to give it focus
- Make sure Caps Lock is off

**Game runs too slowly in Thonny**
- Close other files in Thonny to free memory
- Restart Thonny if the game becomes laggy

**High score not saving**
- Check folder write permissions
- Make sure the game folder is not read-only

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Ideas for Contributions
- [ ] Sound effects and background music
- [ ] Multiple snake skins/themes
- [ ] Multiplayer mode
- [ ] Power-ups (speed boost, invincibility, etc.)
- [ ] Level system with obstacles
- [ ] Mobile-friendly controls
- [ ] Leaderboard system

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Lê Văn Hưng  ( HE186837 : FPT University ) 

## 🙏 Acknowledgments

- Inspired by the classic Nokia Snake game
- Built for educational purposes and Thonny IDE compatibility
- Thanks to the Python and Tkinter communities

## 📊 Statistics

- **Lines of Code**: ~800+
- **Files**: 8 Python modules
- **Features**: 15+ game features
- **Game Modes**: 2 (Wall/Wrap)
- **Speed Levels**: 4
- **Food Types**: 2

## 🔮 Future Updates

- [ ] AI snake opponent
- [ ] Custom level editor
- [ ] Achievement system
- [ ] Replay system
- [ ] Better graphics and animations
- [ ] Configuration GUI

=======================================================

# 🐍 Snake Game Enhanced - Trò Chơi Rắn Săn Mồi Nâng Cấp

Một trò chơi rắn săn mồi hiện đại, đầy tính năng được xây dựng bằng Python và Tkinter, được tối ưu hóa cho các môi trường giáo dục như Thonny IDE.


## ✨ Tính Năng

### 🎮 Chế Độ Chơi
- **Chế Độ Tường**: Gameplay cổ điển - kết thúc game khi đụng tường
- **Chế Độ Xuyên Tường**: Rắn đi xuyên qua tường và xuất hiện ở phía đối diện

### 🍎 Hệ Thống Thức Ăn
- **Thức Ăn Thường** (🔴): Mỗi quả được 10 điểm
- **Thức Ăn Đặc Biệt** (⭐): Ngôi sao vàng được 50 điểm
  - Xuất hiện sau mỗi 5 lần ăn thức ăn thường
  - Biến mất sau 10 giây nếu không được thu thập
  - Làm rắn tăng 2 đốt thay vì 1

### ⚡ Cài Đặt Tốc Độ
- **Chậm**: Độ trễ 200ms - Hoàn hảo cho người mới bắt đầu
- **Trung Bình**: Độ trễ 150ms - Gameplay cân bằng
- **Nhanh**: Độ trễ 100ms - Dành cho người chơi có kinh nghiệm
- **Rất Nhanh**: Độ trễ 50ms - Chế độ thử thách

### 🎯 Tính Năng Game
- **Hệ Thống Điểm Số**: Theo dõi điểm hiện tại và điểm cao nhất
- **Thống Kê**: Thống kê game chi tiết bao gồm số thức ăn đã ăn và thời gian chơi
- **Tạm Dừng/Tiếp Tục**: Nhấn Shift để tạm dừng bất cứ lúc nào
- **Điều Khiển Mượt Mà**: Di chuyển bằng phím mũi tên hoặc WASD
- **Hiệu Ứng Hình Ảnh**: Giao diện hiện đại với gradient và animation
- **Lưu Điểm Cao**: Tự động lưu điểm số tốt nhất của bạn

## 🚀 Bắt Đầu Nhanh

### Yêu Cầu Hệ Thống
- Python 3.7 trở lên
- Tkinter (thường được bao gồm sẵn với Python)

### Cài Đặt

**Chạy game**
   ```bash
   python main.py
   ```

### Dành Cho Người Dùng Thonny
1. Tải tất cả các file Python về một thư mục
2. Mở `main.py` trong Thonny
3. Nhấn F5 hoặc click nút Run
4. Tận hưởng game!

## 🎮 Điều Khiển

| Phím | Chức Năng |
|------|-----------|
| `↑` `↓` `←` `→` | Di chuyển rắn |
| `W` `A` `S` `D` | Di chuyển thay thế |
| `Shift` | Tạm dừng/Tiếp tục game |
| `Q` / `Esc` | Thoát game |
| `R` | Chơi lại (khi game over) |

## 📁 Cấu Trúc Dự Án

```
snake-game-enhanced/
│
├── main.py              # Vòng lặp game chính và điểm khởi đầu
├── snake.py             # Lớp Snake với logic di chuyển và va chạm
├── food_manager.py      # Hệ thống spawn và quản lý thức ăn
├── ui_manager.py        # Giao diện người dùng và rendering
├── input_manager.py     # Xử lý input bàn phím
├── game_state.py        # Trạng thái game và hệ thống điểm số
├── game_object.py       # Lớp cơ sở cho tất cả đối tượng game
├── constants.py         # Cấu hình game và hằng số
├── README.md           # File README tiếng Anh
├── README_VI.md        # File README này (tiếng Việt)
└── snake_highscore.json # Lưu trữ điểm cao (tự động tạo)
```

## 🛠️ Chi Tiết Kỹ Thuật

### Kiến Trúc
- **Thiết Kế Hướng Đối Tượng**: Phân tách rõ ràng các chức năng
- **Cấu Trúc Modular**: Mỗi component trong file riêng biệt
- **Xử Lý Lỗi**: Xử lý lỗi mạnh mẽ để đảm bảo ổn định
- **Quản Lý Resource**: Cleanup và quản lý memory đúng cách

### Các Lớp Chính
- `SnakeGame`: Controller game chính
- `Snake`: Entity rắn với phát hiện di chuyển và va chạm
- `FoodManager`: Xử lý cả thức ăn thường và đặc biệt
- `UIManager`: Quản lý tất cả elements UI và rendering
- `GameState`: Theo dõi điểm số, thống kê và trạng thái game
- `InputManager`: Xử lý input bàn phím với buffering

### Tối Ưu Hóa Performance
- Giới hạn frame rate (~60 FPS)
- Phát hiện va chạm hiệu quả
- Quản lý memory cho phiên chơi dài
- Tối ưu cho môi trường Thonny IDE

## 🏆 Hệ Thống Điểm Số

| Vật Phẩm | Điểm | Tăng Trưởng | Hiệu Ứng Đặc Biệt |
|----------|------|-------------|-------------------|
| Thức Ăn Thường 🔴 | 10 | +1 đốt | Kích hoạt thức ăn đặc biệt mỗi 5 lần ăn |
| Thức Ăn Đặc Biệt ⭐ | 50 | +2 đốt | Có thời hạn (10 giây) |


## 🐛 Khắc Phục Sự Cố

### Các Vấn Đề Thường Gặp

**Cửa sổ game không xuất hiện**
- Đảm bảo Tkinter đã được cài đặt: `python -m tkinter`
- Thử chạy với `python3 main.py` trên macOS/Linux

**Điều khiển không phản hồi**
- Click vào cửa sổ game để đưa nó vào focus
- Đảm bảo Caps Lock đã tắt

**Game chạy quá chậm trong Thonny**
- Đóng các file khác trong Thonny để giải phóng memory
- Restart Thonny nếu game bị lag

**Điểm cao không được lưu**
- Kiểm tra quyền ghi thư mục
- Đảm bảo thư mục game không ở chế độ read-only

## 🤝 Đóng Góp

Chúng tôi hoan nghênh các đóng góp! Đây là cách bạn có thể giúp đỡ:

1. **Fork repository**
2. **Tạo feature branch** (`git checkout -b feature/tinh-nang-tuyet-voi`)
3. **Commit thay đổi** (`git commit -m 'Thêm tính năng tuyệt vời'`)
4. **Push lên branch** (`git push origin feature/tinh-nang-tuyet-voi`)
5. **Mở Pull Request**

### Ý Tưởng Đóng Góp
- [ ] Hiệu ứng âm thanh và nhạc nền
- [ ] Nhiều skin/theme cho rắn
- [ ] Chế độ nhiều người chơi
- [ ] Power-ups (tăng tốc, bất tử, v.v.)
- [ ] Hệ thống level với chướng ngại vật
- [ ] Điều khiển thân thiện với mobile
- [ ] Hệ thống bảng xếp hạng

## 📝 Giấy Phép

Dự án này được cấp phép theo MIT License - xem file [LICENSE](LICENSE) để biết chi tiết.


## 🙏 Lời Cảm Ơn

- Lấy cảm hứng từ game Snake cổ điển của Nokia
- Được xây dựng cho mục đích giáo dục và tương thích với Thonny IDE
- Cảm ơn cộng đồng Python và Tkinter

## 📊 Thống Kê

- **Số Dòng Code**: 800+
- **Số File**: 8 module Python
- **Tính Năng**: 15+ tính năng game
- **Chế Độ Game**: 2 (Tường/Xuyên Tường)
- **Mức Tốc Độ**: 4
- **Loại Thức Ăn**: 2

## 🔮 Cập Nhật Tương Lai

- [ ] AI rắn đối thủ
- [ ] Trình chỉnh sửa level tùy chỉnh
- [ ] Hệ thống thành tích
- [ ] Hệ thống replay
- [ ] Đồ họa và animation tốt hơn
- [ ] GUI cấu hình

## 🎓 Mục Đích Giáo Dục

Game này được thiết kế đặc biệt để:
- **Học lập trình Python**: Code dễ hiểu, có comment tiếng Việt
- **Thực hành OOP**: Ví dụ thực tế về lập trình hướng đối tượng
- **Tương thích Thonny**: Chạy mượt mà trên IDE phổ biến trong giáo dục
- **Tài liệu đầy đủ**: README và comment song ngữ

## 🌟 Các Tính Năng Nổi Bật

### 🎨 **Giao Diện Đẹp Mắt**
- Theme tối hiện đại
- Hiệu ứng gradient cho rắn
- Animation mượt mà
- Icons và emoji sinh động

### 🧠 **Logic Game Thông Minh**
- Collision detection chính xác
- Spawn thức ăn thông minh (không trùng vị trí)
- Buffer input để tránh mất lệnh
- Auto-save điểm cao

### 🔧 **Tối Ưu Hiệu Suất**
- Frame rate ổn định
- Memory management tốt
- Error handling toàn diện
- Cleanup resources đúng cách


---

**⭐ Nếu bạn thích game này, hãy cho một star trên GitHub nhé!**

**🐍 Chúc Bạn Chơi Game Vui Vẻ! 🐍**

**Cảm ơn bạn đã sử dụng Snake Game Enhanced! 🚀**

