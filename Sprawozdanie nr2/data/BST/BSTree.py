from typing import Type

from tree.tree import Tree
from src.nodeTypes import BSTNodeType
from .BSTNode import BSTNode


class BST(Tree):

    def __init__(self, input_data: str):
        super().__init__(input_data)
        self.create(self.base)


    def create(self, elements: list[int]) -> None:
        """Create a binary search tree from a list of elements."""
        for value in elements:
            self.root = self._insert(self.root, value)

    def _insert(self, node: BSTNodeType, value: int) -> BSTNode | Type[BSTNode]:
        """Insert a value into the tree."""
        if node is None:
            return BSTNode(value)
        if value < node.key:
            node.left = self._insert(node.left, value)
            node.left.parent = node
        else:
            node.right = self._insert(node.right, value)
            node.right.parent = node
        return node

    def balance(self):
        """Balance tree using DSW algorithm."""
        self.dsw_balance()

