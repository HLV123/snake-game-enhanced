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

    def draw(self, canvas, cell_size):
        """Vẽ đối tượng lên canvas."""
        x1 = self.x * cell_size
        y1 = self.y * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        
        if self.representation == '#':  # Rắn
            color = 'lime' if hasattr(self, 'is_head') and self.is_head else 'green'
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='darkgreen', width=1)
        elif self.representation == '*':  # Mồi
            canvas.create_oval(x1+2, y1+2, x2-2, y2-2, fill='red', outline='darkred', width=2)