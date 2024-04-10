# bsl tree

class BslNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BslTree:
    def __init__(self):
        self.root = None
        self.base = [2, 5, 10, 12, 13, 6, 9]
        self.create_tree()
        print(self.root)

    def create_tree(self):
        for i in self.base:
            self.insert(i)

    def insert(self, key):
        new_node = BslNode(key)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if key < current.key:
                    if current.left is None:
                        current.left = new_node
                        new_node.parent = current
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        new_node.parent = current
                        break
                    current = current.right


