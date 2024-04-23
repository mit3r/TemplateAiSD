from nodeTypes import BSTNodeType, AVLNodeType


class Rotator:
    @staticmethod
    def rotate_right(node: BSTNodeType | AVLNodeType) -> BSTNodeType | AVLNodeType | None:
        """Rotate right"""
        if node is None or node.left is None:
            return node
        left_node: BSTNodeType | AVLNodeType = node.left
        node.left = left_node.right
        left_node.right = node
        return left_node

    @staticmethod
    def rotate_left(node: BSTNodeType | AVLNodeType) -> BSTNodeType | AVLNodeType | None:
        """Rotate left"""
        if node is None or node.right is None:
            return node
        right_node: BSTNodeType | AVLNodeType = node.right
        node.right = right_node.left
        right_node.left = node
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
