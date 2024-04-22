import gc
from tree import Tree
from BSTNode import BSTNode

class BSTree(Tree):

    def __init__(self, arr: list[int]):
        self.base: list[int] = arr
        self.root: BSTNode | None = None
        self.create(self.base)

    def create(self, elements):
        for value in elements:
            self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return BSTNode(value)
        if value < node.key:
            node.left = self._insert(node.left, value)
            node.left.parent = node
        else:
            node.right = self._insert(node.right, value)
            node.right.parent = node
        return node

    def find_min(self) -> int:
        node: BSTNode = self.root
        temp: int = node.key
        while node.left is not None:
            if node.key < temp:
                temp: int = node.key
            node: BSTNode = node.left
        if node.key < temp:
            temp: int = node.key
        return temp

    def find_max(self) -> int:
        node: BSTNode = self.root
        temp: int = node.key
        while node.right is not None:
            if node.key > temp:
                temp: int = node.key
            node: BSTNode = node.right
        if node.key > temp:
            temp: int = node.key
        return temp

    def find_node(self, key: int) -> BSTNode | None:
        node: BSTNode = self.root
        while node is not None:
            if node.key == key:
                return node
            elif node.key < key:
                node: BSTNode = node.right
            else:
                node: BSTNode = node.left
        return None

    def delete_nodes(self, key_arr: list[int]):
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
            node.key = self.find_min()
            node.right = self.delete_node(node.right, node.key)
        return node

    def delete_all_tree(self, node, first=True):
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

    def dsw_balance(self):
        self.root = self._make_vine(self.root)
        in_order = self._get_in_order_tree(self.root)[1::2]
        in_order = in_order[::-1]
        self.display()
        print(in_order)
        for i in in_order:
            self.root = self.rotate_left(self.find_node(i))
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


if __name__ == '__main__':
    tree = BSTree([8, 2, 5, 14, 10, 12, 13, 2222, 9])
    tree.print_tree()
    print('\n')
    tree.display()

    # tree.delete_nodes([8, 2, 5, 14, 10, 12, 13, 2222, 9])
    tree.dsw_balance()
    tree.display()
