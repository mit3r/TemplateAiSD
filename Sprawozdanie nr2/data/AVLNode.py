from typing import Union


class AVLNode:
    left = None
    right = None

    def __init__(self, key: int):
        self.key: int | None = key
        self.left: Union[AVLNode, None] = None
        self.right: Union[AVLNode, None] = None
        self.height: int = -1

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return f"AVLNode(left={self.left}, right={self.right}, key={self.key}, height={self.height})"
