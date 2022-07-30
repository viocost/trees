from bst import TreeNode


class DrawNode:
    def __init__(self, node: TreeNode, offset=0) -> None:
        self.node = node
        self.offset = offset

        self.left = None
        self.right = None
        self.width = 1
        self.left_width = 0
        self.right_width = 0

        if node.right is not None:
            self.right = DrawNode(node.right, offset+1)
            self.width += self.right.width
            self.right_width = self.right.width

        if node.left is not None:
            self.left = DrawNode(node.left, offset-1)
            self.width += self.left.width
            self.left_width = self.left.width

    def walk(self):
        print(f'\nNode {self.node.value}')
        print(f'  width: {self.width}')
        print(f'  left_width: {self.left_width}')
        print(f'  right_width: {self.right_width}')

        if self.left:
            self.left.walk()

        if self.right:
            self.right.walk()


def draw(root: DrawNode):
    pass

if __name__ == "__main__":
    print("\n\nT1")
    root = TreeNode(14, TreeNode(2, TreeNode(6, TreeNode(7))), TreeNode(5, TreeNode(1, TreeNode(9)), TreeNode(13, TreeNode(4), TreeNode(8))))
    wrapped = DrawNode(root)
    wrapped.walk()

    print("\n\nT2")
    root = TreeNode(1, TreeNode(1234, TreeNode(123, TreeNode(23413)) ), TreeNode(129, TreeNode(32, TreeNode(3, TreeNode(5))), TreeNode(234)))

    wrapped = DrawNode(root)
    wrapped.walk()
