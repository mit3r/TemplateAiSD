class AVLNode:
    def __init__(self, key: int):
        self.key: int | None = None
        self.left: AVLNode | None = None
        self.right: AVLNode | None = None
        self.height: int = -1

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return f"AVLNode(left={self.left}, right={self.right}, key={self.key}, height={self.height})"
