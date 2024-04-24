import gc
from .Printer import Printer
from src.nodeTypes import AVLNodeType, BSTNodeType
from .Finder import Finder
from .Rotator import Rotator


def input_to_arr(input_str: str) -> list[int]:
    """Convert input string to list of integers."""
    return list(map(int, input_str.split(',')))


class Tree(Printer, Finder, Rotator):
    def __init__(self, input_data: str):
        self.base: list[int] = input_to_arr(input_data)
        self.root: BSTNodeType | AVLNodeType | None = None
        self._print_stat()

    def _print_stat(self) -> None:
        """Print sorted keys and median of the array."""
        stat = self._sort_keys_and_median(self.base)
        print(f"Sorted: {stat[0]}")
        print(f"key median: {stat[1]}")

    def dsw_balance(self):
        """ Balance tree using DSW algorithm.
        1. Create vine
        2. Get in order
        3. Rotate left by key from in order
        4. Display
        """
        self.root = self._make_vine(self.root)
        in_order = self._get_in_order_tree(self.root)

        for i in in_order[::2]:
            self.rotate_left_by_key(i)

        self.rotate_left_by_key(in_order[1])
        self.display()
        print(self._get_pre_order_tree(self.root))

    def delete_nodes(self, input_data: str):
        """Delete nodes from the tree."""
        key_arr = input_to_arr(input_data)
        for key in key_arr:
            self.root = self.delete_node(self.root, key)

    def delete_node(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self.delete_node(node.left, key)
        elif key > node.key:
            node.right = self.delete_node(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.key = self.find_min(self.root)
            node.right = self.delete_node(node.right, node.key)
        return node

    def delete_all_tree(self, node: BSTNodeType, first=True):
        if first:
            print("Deleting all tree: ", end='')
            node = self.root

        if node is None:
            return

        self.delete_all_tree(node.left, first=False)
        self.delete_all_tree(node.right, first=False)
        print(node.key, end=' ')
        self.root = self.delete_node(self.root, node.key)
        gc.collect()

    def _sort_keys_and_median(self, arr: list[int]) -> tuple[list[int], int | float | None]:
        """Sort keys and return median of the array."""
        arr = sorted(arr)
        return arr, self._find_median(arr)
