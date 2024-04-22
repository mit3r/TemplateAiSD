import gc
class BSTNode:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
        self.parent = None


class BSTree:

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

    def print_tree(self):
        print("Pre order: ", end='')
        self.print_pre_order_tree(self.root)
        print("\nIn order: ", end='')
        self._print_in_order_tree(self.root)
        print("\nPost order: ", end='')
        self._print_post_order_tree(self.root)

    def print_pre_order_tree(self, node):
        if node is not None:
            print(node.key, end=' ')
            self.print_pre_order_tree(node.left)
            self.print_pre_order_tree(node.right)

    def _print_in_order_tree(self, node):
        if node is not None:
            self._print_in_order_tree(node.left)
            print(node.key, end=' ')
            self._print_in_order_tree(node.right)

    def _print_post_order_tree(self, node):
        if node is not None:
            self._print_in_order_tree(node.left)
            self._print_in_order_tree(node.right)
            print(node.key, end=' ')

    @staticmethod
    def find_min(root) -> int:
        node: BSTNode = root
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
            node.key = self.find_min(node.right)
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
        self.delete_node(self.root, node.key)


if __name__ == '__main__':
    tree = BSTree([8, 2, 5, 14, 10, 12, 13, 2222, 9])
    tree.print_tree()
    print('\n')
    # tree.delete_nodes([8, 2, 5, 14, 10, 12, 13, 2222, 9])
    tree.delete_all_tree(tree.root)
    tree.print_tree()
