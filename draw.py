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
        print(f'{self.node.value}, width: {self.width}, offset: {self.offset}, width left: {self.left_width}, width right: {self.right_width}')
        if self.left:
            self.left.walk()

        if self.right:
            self.right.walk()





def draw_bst(node):
    wrapped = DrawNode(node)


if __name__ == "__main__":
    root = TreeNode(14, TreeNode(2, TreeNode(6, TreeNode(7))), TreeNode(5, TreeNode(1, TreeNode(9)), TreeNode(13, TreeNode(4), TreeNode(8))))
    wrapped = DrawNode(root)
    wrapped.walk()
