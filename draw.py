from bst import TreeNode
from enum import Enum


class DrawNode:
    def __init__(self, node: TreeNode, offset=0, level = 0) -> None:
        self.node = node
        self.offset = offset
        self.level = level

        self.extension_left = 0
        self.extension_right = 0

        self.left = None
        self.right = None
        self.width = len(node)
        self.value_width = len(node)
        self.left_width = 0
        self.right_width = 0

        self.edges = {
            EdgeDirection.RIGHT: type(Edge),
            EdgeDirection.LEFT: type(Edge)
        }

        if node.right is not None:
            self.edges[EdgeDirection.RIGHT] = Edge(EdgeDirection.RIGHT, self.get_base_edge_offset_right())
            self.right = DrawNode(node.right, offset+1, level + 1)
            self.width += self.right.width
            self.right_width = self.right.width
            # self.extension_right = max(-1 * (self.value_width - self.right.left_width), 0)

        if node.left is not None:
            self.left = DrawNode(node.left, offset-1, level + 1)
            self.width += self.left.width
            self.left_width = self.left.width
            self.extension_left = max(-1 * (self.value_width - self.left.right_width), 0)

    def get_base_edge_offset_right(self):
        if self.value_width % 2 == 1:
            return self.get_base_edge_offset_left() + 2

    def get_base_edge_offset_left(self):

        if self.value_width % 2 == 1:
            return (self.offset + self.value_width) - self.value_width // 2

        return (self.offset + self.value_width) - self.value_width // 2


    def get_left_child_offset(self, value_length, edge_offset):
        if value_length % 2 == 1:
            return edge_offset - 1 - (value_length // 2)

        return  edge_offset - (value_length // 2)

    def get_right_child_offset(self, value_length, edge_offset):
        if value_length % 2 == 1:
            return edge_offset + 1 - (value_length // 2)
        return edge_offset - value_length // 2

    def __str__(self):
        return "_" * self.extension_left + f"{self.node.value}" + "_" * self.extension_right

    def __repr__(self) -> str:
        return f"Node: {self.node.value}"

    def walk(self):
        # print(f'\nNode {self}')
        # print(f'  width: {self.width}')
        # print(f'  left_width: {self.left_width}')
        # print(f'  right_width: {self.right_width}')

        if self.left:
            self.left.walk()

        if self.right:
            self.right.walk()



class EdgeDirection(Enum):
    RIGHT = 0
    LEFT = 1


class Edge:
    def __init__(self, direction: EdgeDirection, offset: int) -> None:
        self.direction = direction
        self.offset = offset


def build_levels(root: DrawNode):
    result = []

    queue = [root]

    while len(queue) > 0:
        node = queue.pop(0)

        print(node.node.value)

        if len(result) - 1 < node.level:
            result.append([])

        result[node.level].append(node)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    print(result)


    return result

def draw(root: DrawNode):

    pass

def draw_aux(nodes, edges, canvas_width):
    if len(nodes) == 0:
        return
    if len(edges) == 0:
        pass
    line = ""




def main():
    print("\n\nT1")
    root = TreeNode(14, TreeNode(2, TreeNode(6, TreeNode(7))), TreeNode(5, TreeNode(1, TreeNode(9)), TreeNode(13, TreeNode(4), TreeNode(8))))
    wrapped = DrawNode(root)
    wrapped.walk()

    print("In order")
    build_levels(wrapped)

    print("\n\nT2")
    root = TreeNode(1, TreeNode(1234, TreeNode(123, TreeNode(23413)) ), TreeNode(129, TreeNode(32, TreeNode(3, TreeNode(5))), TreeNode(234)))


    wrapped = DrawNode(root)
    wrapped.walk()

if __name__ == "__main__":
    main()

main()
