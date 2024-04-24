from src.nodeTypes import BSTNodeType, AVLNodeType


class Rotator:
    def rotate_right(self,node: BSTNodeType | AVLNodeType) -> BSTNodeType | AVLNodeType | None:
        """Rotate right"""
        if node is None or node.left is None:
            return node
        left_node: BSTNodeType | AVLNodeType = node.left
        node.left = left_node.right
        left_node.right = node
        if self.__class__ == "AVL":
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
            left_node.height = 1 + max(self._get_height(left_node.left), self._get_height(left_node.right))
        return left_node

    def rotate_left(self,node: BSTNodeType | AVLNodeType) -> BSTNodeType | AVLNodeType | None:
        """Rotate left"""
        if node is None or node.right is None:
            return node
        right_node: BSTNodeType | AVLNodeType = node.right
        node.right = right_node.left
        right_node.left = node
        if self.__class__.__name__ == "AVL":
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
            right_node.height = 1 + max(self._get_height(right_node.left), self._get_height(right_node.right))
        return right_node

    def rotate_left_by_key(self, key: int) -> None:
        """Rotate left by key"""
        self.root = self._rotate_left_by_key(self.root, key)

    def _rotate_left_by_key(self, node, key):
        """Rotate left by key recursively"""
        if node is None:
            return None
        if key < node.key:
            node.left = self._rotate_left_by_key(node.left, key)
        elif key > node.key:
            node.right = self._rotate_left_by_key(node.right, key)
        else:
            return self.rotate_left(node)
        return node

    def _make_vine(self, node: BSTNodeType | AVLNodeType | None) -> BSTNodeType | AVLNodeType | None:
        """Create vine"""
        if node is None:
            return None
        while node.left is not None:
            node = self.rotate_right(node)
        node.right = self._make_vine(node.right)
        return node
