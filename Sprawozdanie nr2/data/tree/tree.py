import gc
from .Printer import Printer
from src.nodeTypes import AVLNodeType, BSTNodeType
from .Finder import Finder
from .Rotator import Rotator
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
txt_file_path = os.path.join(current_directory, 'tree.tex')


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
        print(in_order[::2])
        print(in_order[1::2])
        for i in in_order[::2]:
            self.rotate_left_by_key(i)

        for i in in_order[1::2]:
            if abs((self._calculate_height(self.root.left)) - (self._calculate_height(self.root.right) + 1)) <= 1:
                break
            self.rotate_left_by_key(i)

    def delete_nodes(self, input_data: str) -> None:
        """Delete nodes from the tree."""
        key_arr: list[int] = input_to_arr(input_data)
        for key in key_arr:
            self.root = self._delete_node(self.root, key)
        if self.__class__.__name__ == 'AVL':
            self.dsw_balance()
            print("Tree has been rebalanced using DSW algorithm")

    def _delete_node(self, node: 'BSTNodeType | AVLNodeType | None', key: int) -> BSTNodeType | AVLNodeType | None:
        """Delete node by key."""
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
        """Delete all nodes by post order."""
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

    def _calculate_height(self, node: BSTNodeType | AVLNodeType | None = None) -> int:
        """Calculate height of the node recursively. """
        if node is None:
            return -1
        return 1 + max(self._calculate_height(node.left), self._calculate_height(node.right))

    def export_tree(self):
        self.latex_code = ("\\documentclass{article}\n\\usepackage{tikz}\n\\usetikzlibrary{shapes,"
                           "positioning}\n\\begin{document}\n\\begin{tikzpicture}\n")
        self.latex_code += ("[ every node/.style={circle,draw,minimum size=10mm, font=\Large, inner sep=1mm, "
                            "fill=red, text=white}, "
                            "level/.style={sibling distance=50mm/#1}, level 2/.style={sibling distance=30mm}, "
                            "level 3/.style={sibling distance=20mm}, thick ]")

        self._traverse(self.root)
        self.latex_code += ";\n\\end{tikzpicture}\n\\end{document}"
        with open(txt_file_path, "w") as file:
            file.write(self.latex_code)

    def _traverse(self, node):
        if node is not None:
            self.latex_code += f"  \\node {{ {node.key} }}\n"
            if node.left is not None:
                self.latex_code += "    child { "
                self._traverse(node.left)
                self.latex_code += " }\n"
            if node.right is not None:
                self.latex_code += "    child { "
                self._traverse(node.right)
                self.latex_code += " }\n"
