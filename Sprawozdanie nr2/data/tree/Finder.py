from src.nodeTypes import BSTNodeType, AVLNodeType


class Finder:
    @staticmethod
    def find_min(node) -> int:
        """Find minimum value in the tree."""
        temp: int = node.key
        while node.left is not None:
            if node.key < temp:
                temp: int = node.key
            node: BSTNodeType = node.left
        if node.key < temp:
            temp: int = node.key
        return temp

    @staticmethod
    def find_max(node) -> int:
        temp: int = node.key
        while node.right is not None:
            if node.key > temp:
                temp: int = node.key
            node: BSTNodeType = node.right
        if node.key > temp:
            temp: int = node.key
        return temp

    @staticmethod
    def find_node_by_key(node: BSTNodeType | AVLNodeType, key: int) -> BSTNodeType | None:
        while node is not None:
            if node.key == key:
                return node
            elif node.key < key:
                node: BSTNodeType = node.right
            else:
                node: BSTNodeType = node.left
        return None

    @staticmethod
    def _find_median(arr: list[int]) -> int:
        """Return median of the array."""
        if len(arr) % 2 == 0:
            return arr[len(arr) // 2]
        else:
            return (arr[len(arr) // 2] + arr[len(arr) // 2 + 1]) // 2

    def _get_height(self, node: BSTNodeType | AVLNodeType | None) -> int:
        """Get height of the node."""
        if node is None:
            return -1
        return node.height

