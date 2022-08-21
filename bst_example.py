from lib.bst import BSTNode
from lib.draw import draw
from lib.bst import Sequence

def main():
    tree1 = BSTNode(7, BSTNode(3, BSTNode(1, BSTNode(0), BSTNode(2)), BSTNode(5, BSTNode(4), BSTNode(6))), BSTNode(17, BSTNode(11, BSTNode(9), BSTNode(15 )), BSTNode(25, BSTNode(20, BSTNode(19)), BSTNode(27))))
    seq = Sequence(tree1)
    seq.delete(17)
    draw(*seq.snapshots)


    tree2 = BSTNode(7, BSTNode(3, BSTNode(1, BSTNode(0), BSTNode(2)), BSTNode(5, BSTNode(4), BSTNode(6))), BSTNode(17, BSTNode(11, BSTNode(9), BSTNode(15 )), BSTNode(25, BSTNode(20, None, BSTNode(21, None, BSTNode(22))), BSTNode(27))))
    s2 = Sequence(tree2)
    s2.delete(17)

    draw(*s2.snapshots)
    draw(s2.snapshots[0])
    draw(s2.snapshots[1])
if __name__ == "__main__":

    main()
