from lib.bt import TreeNode, set_parent
from lib.draw import draw
from copy import deepcopy

class BSTNode(TreeNode):

    def __init__(self, value, left=None, right=None, color=None, count=1, inversed=False) -> None:
        super().__init__(value, left, right, color)
        self.inversed = inversed
        self.count = count


    def clone(self):
        return deepcopy(self)

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


    def find(self, value):
        print(f"Searching {value} on {self} {self.left} {self.right} parent {self.parent}")
        node = self
        while node is not None:
            if node._value == value:
                return node
            if node.inversed:
                node = node.right if  value < node._value else node.left
            else:
                node = node.left if value < node._value else node.right


    @property
    def leftmost(self):
        if not self.left:
            return self
        return self.left.leftmost

    @property
    def rightmost(self):
        if not self.right:
            return self
        return self.right.rightmost

    @property
    def min(self):
        if self.inversed:
            return self.rightmost
        return self.leftmost

    @property
    def max(self):
        if self.inversed:
            return self.leftmost
        return self.rightmost

    @property
    def is_root(self):
        return not self.parent

    @property
    def root(self):
        if not self.parent:
            return self
        return self.parent.root

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
                self.left = set_parent(self, node)
                print(f"{node}: Parent: {node.parent}")

        if ((node > self) ^ self.inversed):
            if self.right:
                self.right.insert(node)
            else:
                self.right = set_parent(self, node)
                print(f"{node}: Parent: {node.parent}")

    def delete(self, value):
        node = self.find(value)
        # nothing to delete
        if not node:
            return None

        # just decrement the count if there are duplicates
        if node.count > 1:
            node.count -= 1
            return node.root, node

        # only left subtree exists
        if node.left and not node.right:
            node.left.parent = node.parent
            if node.parent:
                node.parent.replace_child(node, node.left)
            return node.left.root, node

        # only right subtree exists
        if node.right and not node.left:
            node.right.parent = node.parent
            if node.parent:
                node.parent.replace_child(node, node.right)
            return node.right.root, node

        # just setting parent value to None for this child
        if not node.right and not node.left:

            print(f'deleting leaf {node} with parent {node.parent}')
            if node.parent is None:
                print("No parent")
                return None, node
            root = node.root
            node.parent.replace_child(node, None)
            return root, node


        if node.right.left:
            right_leftmost = node.right.leftmost.clone()
            right_leftmost.left = node.left
            right_leftmost.right = node.right
            right_leftmost.parent = node.parent
            if node.parent:
                node.parent.replace_child(node, right_leftmost)
            node.right.delete(right_leftmost._value)
            return right_leftmost.root, node



        node.right.parent = node.parent
        node.right.left = node.left
        if node.parent:
            node.parent.replace_child(node, node.right)
        return node.right.root, node




    def replace_child(self, child,  new_child):
        if child is self.right:
            self.right = new_child
        elif child is self.left:
            self.left = new_child
        else:
            raise ValueError(f"{child} is not a child of {self}")







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

    def delete(self, value):
        print(f"Deleting {value}")
        new_tree = self.snapshots[-1].clone()
        res = new_tree.delete(value)
        print(str(res))

        if not res:
            self.snapshots.append(new_tree)
            return
        self.snapshots.append(res[0])



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
    # seq2.delete(-4)


    draw(*seq2.snapshots)

    print(seq2.snapshots[-1].find(4))

    seq3 = Sequence(BSTNode(2))
    # seq3.insert(BSTNode(1))
    # seq3.insert(BSTNode(3))
    # seq3.delete(2)


    seq4 = Sequence(BSTNode(2))
    seq4.insert(BSTNode(1))
    seq4.insert(BSTNode(3))
    # seq4.inverse()

    seq4.delete(1)
    draw(*seq4.snapshots)

    print(BSTNode(4).root)

if __name__ == "__main__":
    main()
