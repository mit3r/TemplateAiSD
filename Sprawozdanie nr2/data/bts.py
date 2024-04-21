from utils import UtilsMethods


class BTSNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BSTTree:
    def __init__(self):
        self.root = None
        # self.base = UtilsMethods.int_list(input("Enter the base of the BST tree: ").split(' '))
        self.base = [8, 2, 5, 14, 1, 10, 12, 13, 6, 9]
        self.create(self.base)
        print(self.root)
        self.print_tree()

    def create(self, elements):
        for value in elements:
            self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return BTSNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
            node.left.parent = node
        else:
            node.right = self._insert(node.right, value)
            node.right.parent = node
        return node


    def print_tree(self):
        # print("In order: ", end="")
        self._print_in_order_tree(self.root)
        # print("\nPost order: ", end="")
        # self._print_pre_order_tree(self.root)
        # print("\nPre order: ", end="")
        # self._print_post_order_tree(self.root)

    def _print_in_order_tree(self, node):
        if node is not None:
            self._print_in_order_tree(node.left)
            print(node.value,end='')
            if node.left is not None:
                print(" left: ",node.left.value,end="")
            if node.right is not None:
                print(" right: ",node.right.value,end="")
            print('\n')
            self._print_in_order_tree(node.right)

    def _print_pre_order_tree(self, node):
        if node is not None:
            print(node.value, end=" ")
            self._print_pre_order_tree(node.left)
            self._print_pre_order_tree(node.right)

    def _print_post_order_tree(self, node):
        if node is not None:
            self._print_post_order_tree(node.left)
            self._print_post_order_tree(node.right)
            print(node.value, end=" ")

# Przykładowe użycie
bst = BSTTree()



