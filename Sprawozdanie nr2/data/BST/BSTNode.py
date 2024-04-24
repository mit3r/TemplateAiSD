from typing import Union


class BSTNode:
    key = None
    right = None
    left = None
    parent = None

    def __init__(self, value: int):
        self.key: int = value
        self.left: Union[BSTNode, None] = None
        self.right: Union[BSTNode, None] = None
        self.parent: Union[BSTNode, None] = None
