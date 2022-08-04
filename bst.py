from bt import TreeNode
from draw import draw

class BSTNode(TreeNode):

    def __init__(self, value, left=None, right=None, color=None, count=1, inversed=False) -> None:
        super().__init__(value, left, right, color)
        self.inversed = inversed
        self.count = count


    def clone(self):
        root = BSTNode(self._value, color=self.color, count=self.count, inversed=self.inversed)
        if self.left:
            root.left = self.left.clone()
        if self.right:
            root.right = self.right.clone()
        return root

    def inverse(self):
        self.inversed = not self.inversed
        self.right, self.left = self.left, self.right

        if self.right:
            self.right.inverse()

        if self.left:
            self.left.inverse()
        return self

    @property
    def value(self):
        return str(self)

    def __str__(self) -> str:
        if self.count > 1:
            return f"{self._value}({self.count})"
        return str(self._value)


    def insert(self, value):

        node = value
        if type(value) != self.__class__:
            node = self.__class__(value, inversed=self.inversed)

        if node == self:
            self.count += 1
            return

        if ((node < self) ^ self.inversed):
            if self.left:
                self.left.insert(node)
            else:
                self.left = node

        if ((node > self) ^ self.inversed):
            if self.right:
                self.right.insert(node)
            else:
                self.right = node

class Sequence:
    def __init__(self, root: BSTNode) -> None:
        self.snapshots = [root]

    def insert(self, value):
        new_tree = self.snapshots[-1].clone()
        new_tree.insert(value)
        self.snapshots.append(new_tree)

    def inverse(self):
        new_tree = self.snapshots[-1].clone()
        new_tree.inverse()
        self.snapshots.append(new_tree)

def main():
    bst = BSTNode(5, BSTNode(3), BSTNode(8))

    seq = Sequence(bst)

    seq.insert(BSTNode(4, color=1)),
    seq.insert(BSTNode(1, color=2)),
    seq.insert(BSTNode(-1, color=2)),
    seq.insert(BSTNode(-91, color=2)),
    seq.insert(BSTNode(9, color=3)),
    seq.insert(BSTNode(7, color=4))
    seq.insert(BSTNode(7, color=4))
    seq.insert(BSTNode(7, color=4))
    seq.inverse()

    draw(*seq.snapshots)

    seq2 = Sequence(BSTNode(1))
    seq2.insert(BSTNode(2))
    seq2.insert(BSTNode(3))
    seq2.insert(BSTNode(4))
    seq2.insert(BSTNode(4))
    seq2.insert(BSTNode(4))
    seq2.insert(BSTNode(4))
    seq2.insert(BSTNode(4))
    seq2.insert(BSTNode(4))
    seq2.insert(BSTNode(4))
    seq2.inverse()
    seq2.insert(BSTNode(-4))
    seq2.insert(BSTNode(40))

    draw(*seq2.snapshots)

if __name__ == "__main__":
    main()
