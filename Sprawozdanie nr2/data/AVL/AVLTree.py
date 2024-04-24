from .AVLNode import AVLNode
from tree.tree import Tree
from src.nodeTypes import BSTNodeType, AVLNodeType


class AVL(Tree):
    def __init__(self, input_data: str, build: bool = True, obj: BSTNodeType | None = None):
        if build:
            super().__init__(input_data)
            self.create()
        elif not build and obj is not None:
            self.base = []
            self.root: AVLNodeType | None = self.convert_bst_to_avl(obj=obj)
            self.calculate_height()
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

    def create(self):
        pass

    def balance(self):
        """Balance tree using DSW algorithm."""
        self.dsw_balance()

    def calculate_height(self):
        """Calculate height of the tree."""
        self.root.height = self._calculate_height(self.root)

    def _calculate_height(self, node):
        """Calculate height of the node recursively. """
        if node is None:
            return -1
        return 1 + max(self._calculate_height(node.left), self._calculate_height(node.right))


