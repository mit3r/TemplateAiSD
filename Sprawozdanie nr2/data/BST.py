import gc
from tree import Tree
from BSTNode import BSTNode
from AVL import AVL


class BST(Tree):

    def __init__(self, input_data: str):
        super().__init__(input_data)
        self.create(self.base)

    def create(self, elements):
        """Create a binary search tree from a list of elements."""
        for value in elements:
            self.root = self._insert(self.root, value)

    def _insert(self, node, value):
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
        print(self.__class__.__name__)


if __name__ == '__main__':
    tree = BST("8, 2, 5, 14, 10, 12, 13")
    tree.print_tree(tree.root)
    print('\n')
    tree.display()
    # tree.delete_nodes([8, 2, 5, 14, 10, 12, 13, 2222, 9])
    tree.balance()
    tree.display()
