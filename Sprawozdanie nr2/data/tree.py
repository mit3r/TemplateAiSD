import gc
from AVLNode import AVLNode
from BSTNode import BSTNode

if not gc.isenabled():
    gc.enable()


class Tree:


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
