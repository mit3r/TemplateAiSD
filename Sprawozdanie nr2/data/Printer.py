from nodeTypes import BSTNodeType, AVLNodeType


class Printer:
    def print_tree(self, root: BSTNodeType | AVLNodeType) -> None:
        """Prints tree in pre, in and post order"""
        print("Pre order: ", end='')
        print(self._get_pre_order_tree(root))
        print("\nIn order: ", end='')
        print(self._get_in_order_tree(root))
        print("\nPost order: ", end='')
        print(self._get_post_order_three(root))

    def _get_pre_order_tree(self, node: BSTNodeType | AVLNodeType, arr: list[int] | bool = None, first: bool = True) -> list[int]:
        """Returns list of keys in pre order"""
        if first:
            arr = [] if arr is None else arr
        if node is not None:
            arr.append(node.key)
            self._get_pre_order_tree(node.left, arr, first=False)
            self._get_pre_order_tree(node.right, arr, first=False)
        return arr

    def _get_in_order_tree(self, node: BSTNodeType, arr: list[int] | bool = None, first: bool = True) -> list[int]:
        """Returns list of keys in in-order"""
        if first:
            arr = [] if arr is None else arr
        if node is not None:
            self._get_pre_order_tree(node.left, arr, first=False)
            arr.append(node.key)
            self._get_pre_order_tree(node.right, arr, first=False)
        return arr

    def _get_post_order_three(self, node: BSTNodeType, arr: list[int] | bool = None, first: bool = True) -> list[int]:
        """Returns list of keys in post order"""
        if first:
            arr = [] if arr is None else arr
        if node is not None:
            self._get_pre_order_tree(node.left, arr, first=False)
            self._get_pre_order_tree(node.right, arr, first=False)
            arr.append(node.key)
        return arr

    def display(self):
        """Displays tree"""
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
