from bt import TreeNode
from draw import draw

class BSTNode(TreeNode):

    def __init__(self, value, left=None, right=None, color=None) -> None:
        super().__init__(value, left, right, color)

    def clone(self):
        root = BSTNode(self.value, color=self.color)
        if self.left:
            root.left = self.left.clone()
        if self.right:
            root.right = self.right.clone()
        return root

    def insert(self, value, immutable=True):
        if immutable:
            new_tree = self.clone()
            new_tree.insert(value, False)
            return new_tree

        node = value
        if type(value) != BSTNode:
            node = BSTNode(value)

        if node < self:
            if self.left:
                self.left.insert(node, False)
            else:
                self.left = node

        if node > self:
            if self.right:
                self.right.insert(node, False)
            else:
                self.right = node

class Sequence:
    def __init__(self, root: BSTNode) -> None:
        self.snapshots = [root]

    def insert(self, value):
        self.snapshots.append(self.snapshots[-1].insert(value))

def main():
    bst = BSTNode(5, BSTNode(3), BSTNode(8))

    seq = Sequence(bst)

    seq.insert(BSTNode(4, color=1)),
    seq.insert(BSTNode(1, color=2)),
    seq.insert(BSTNode(9, color=3)),
    seq.insert(BSTNode(7, color=4))

    draw(*seq.snapshots)

if __name__ == "__main__":
    main()
