import gc
from AVLNode import AVLNode
from BSTNode import BSTNode

if not gc.isenabled():
    gc.enable()


class Tree:
    def __init__(self, arr: list[int]):
        self.base: list[int] = arr
        self.root: BSTNode | AVLNode | None = None

    def print_tree(self):
        print("Pre order: ", end='')
        print(self._get_pre_order_tree(self.root))
        print("\nIn order: ", end='')
        print(self._get_in_order_tree(self.root))
        print("\nPost order: ", end='')
        print(self._get_post_order_three(self.root))

    def _get_pre_order_tree(self, node: BSTNode | AVLNode, arr: list[int] | bool = None, first: bool = True) -> list[
        int]:
        if first:
            arr = [] if arr is None else arr
        if node is not None:
            arr.append(node.key)
            self._get_pre_order_tree(node.left, arr, first=False)
            self._get_pre_order_tree(node.right, arr, first=False)
        return arr

    def _get_in_order_tree(self, node: BSTNode, arr: list[int] | bool = None, first: bool = True) -> list[int]:
        if first:
            arr = [] if arr is None else arr
        if node is not None:
            self._get_pre_order_tree(node.left, arr, first=False)
            arr.append(node.key)
            self._get_pre_order_tree(node.right, arr, first=False)
        return arr

    def _get_post_order_three(self, node: BSTNode, arr: list[int] | bool = None, first: bool = True) -> list[int]:
        if first:
            arr = [] if arr is None else arr
        if node is not None:
            self._get_pre_order_tree(node.left, arr, first=False)
            self._get_pre_order_tree(node.right, arr, first=False)
            arr.append(node.key)
        return arr

    @staticmethod
    def rotate_right(node):
        if node is None or node.left is None:
            return node
        left_node = node.left
        node.left = left_node.right
        left_node.right = node
        return left_node

    @staticmethod
    def rotate_left(node):
        if node is None or node.right is None:
            return node
        right_node = node.right  # 4
        node.right = right_node.left  # 3
        right_node.left = node
        return right_node

    def rotate_left_by_key(self, key):
        self.root = self._rotate_left_by_key(self.root, key)

    def _rotate_left_by_key(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._rotate_left_by_key(node.left, key)
        elif key > node.key:
            node.right = self._rotate_left_by_key(node.right, key)
        else:
            return self.rotate_left(node)
        return node

    def dsw_balance(self):
        self.root = self._make_vine(self.root)
        in_order = self._get_in_order_tree(self.root)
        print(in_order)
        self.display()

        for i in in_order[::2]:
            self.rotate_left_by_key(i)
            self.display()

        self.rotate_left_by_key(in_order[1])
        self.display()
        print(self.__class__.__name__)
        if self.__class__.__name__ == 'BSTree':
            print("BSTree balanded, converting into AVL object...")
            self.__class__ = AVLTree
            self.root = AVLNode(self.root.key)
            self.display()



    def _make_vine(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = self.rotate_right(node)
        node.right = self._make_vine(node.right)
        return node

    def display(self):
        if self.root is None:
            print('Tree is empty')
            return
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            key_str = '%s' % node.key
            key_length = len(key_str)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + key_str
            second_line = x * ' ' + '/' + (n - x - 1 + key_length) * ' '
            shifted_lines = [line + key_length * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + key_length, p + 2, n + key_length // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            key_str = '%s' % node.key
            key_length = len(key_str)
            first_line = key_str + x * '_' + (n - x) * ' '
            second_line = (key_length + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [key_length * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + key_length, p + 2, key_length // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        key_str = '%s' % node.key
        key_length = len(key_str)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + key_str + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + key_length + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + key_length * ' ' + b for a, b in zipped_lines]
        return lines, n + m + key_length, max(p, q) + 2, n + key_length // 2
