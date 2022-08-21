from lib.draw import draw

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


n1 = Node(11)
n2 = Node(14)
n3 = Node(4)

n1.right = n2
n1.left = n3

draw(n1)
