# game_object.py

class GameObject:
    """Lớp cơ sở cho tất cả các đối tượng trong game."""
    def __init__(self, x, y, representation):
        self.x = x
        self.y = y
        self.representation = representation

    def get_position(self):
        """Trả về vị trí hiện tại của đối tượng."""
        return (self.x, self.y)

    def draw(self, screen):
        """Vẽ đối tượng lên màn hình."""
        screen.addstr(self.y, self.x, self.representation)