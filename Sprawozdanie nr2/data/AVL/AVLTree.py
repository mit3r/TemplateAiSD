from AVLNode import AVLNode
from .AVLNode import AVLNode
from tree.tree import Tree
from src.nodeTypes import BSTNodeType, AVLNodeType


class AVL(Tree):
    def __init__(self, input_data: str, build: bool = True, obj: BSTNodeType | None = None):
        if build:
            super().__init__(input_data)
            self.root = self.create(sorted(self.base))
        elif not build and obj is not None:
            self.base = []
            self.root: AVLNodeType | None = self.convert_bst_to_avl(obj=obj)
            self._calculate_height()
            self.display()

    def convert_bst_to_avl(self, obj: BSTNodeType) -> AVLNode | None:
        """ Convert BST to AVL. (DSW algorithm has been executed)"""
        if obj is None:
            return None
        node = AVLNode(obj.key)
        self.base.append(obj.key)
        node.left = self.convert_bst_to_avl(obj=obj.left)
        node.right = self.convert_bst_to_avl(obj=obj.right)
        return node

    def create(self, data: list[int] = None) -> AVLNode | None:
        if not data:
            return None
        mid = len(data) // 2
        node = AVLNode(data[mid])
        node.left = self.create(data[:mid])
        node.right = self.create(data[mid + 1:])
        self._calculate_height(node)
        return node

    def balance(self):
        """Balance tree using DSW algorithm."""
        self.dsw_balance()

