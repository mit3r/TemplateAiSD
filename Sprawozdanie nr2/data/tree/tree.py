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
        stat: tuple[list[int], int] = self._sort_keys_and_median(self.base)
        print(f"Sorted: {stat[0]}")
        print(f"key median: {stat[1]}")

    def dsw_balance(self) -> None:
        """ Balance tree using DSW algorithm.
        1. Create vine
        2. Get in order
        3. Rotate left by key from in order
        4. Display
        """
        self.root = self._make_vine(self.root)
        in_order: list[int] = self._get_in_order_tree(self.root)

        for i in in_order[::2]:
            self.rotate_left_by_key(i)

        self.rotate_left_by_key(in_order[1])
        self.display()

    def delete_nodes(self, input_data: str) -> None:
        """Delete nodes from the tree."""
        key_arr: list[int] = input_to_arr(input_data)
        for key in key_arr:
            self.root = self._delete_node(self.root, key)

    def _delete_node(self, node: 'BSTNodeType | AVLNodeType | None', key: int) -> BSTNodeType | AVLNodeType | None:
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_node(node.left, key)
        elif key > node.key:
            node.right = self._delete_node(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.key = self.find_min(node.right)
            node.right = self._delete_node(node.right, node.key)
        return node

    def delete_all_tree(self, node: BSTNodeType | AVLNodeType, first=True):
        if first:
            print("Deleting all tree: ", end='')
            node = self.root

        if node is None:
            return

        self.delete_all_tree(node.left, first=False)
        self.delete_all_tree(node.right, first=False)
        print(node.key, end=' ')
        self.root = self._delete_node(self.root, node.key)
        gc.collect()

    def _sort_keys_and_median(self, arr: list[int]) -> tuple[list[int], int]:
        """Sort keys and return median of the array."""
        arr = sorted(arr)
        return arr, self._find_median(arr)

    def export_tree(self):
        return f"\\node {{{self._export(self.root)}}};"

    def _export(self, node):
        if not node.left and not node.right:
            return f"node {{{node.key}}}"
        l_str = f"child {self._export(node.left)}" if node.left else "child[missing]"
        r_str = f"child {self._export(node.right)}" if node.right else "child[missing]"
        return f"node {{{node.key}}} {l_str} {r_str}"
