from bst import TreeNode
from enum import Enum


class EdgeDirection(Enum):
    RIGHT = 0
    LEFT = 1

PIVOT_MARGIN = 2
LEFT_MARGIN = 2


class Edge:
    def __init__(self, direction: EdgeDirection, position: int) -> None:
        self.direction = direction
        self._position = position
        self.offset = 0

    @property
    def position(self):
        return self.offset + self._position

    def move(self, offset):
        self.offset += offset

    def __str__(self) -> str:
        return "/" if self.direction == EdgeDirection.LEFT else "\\"

class Edges:
    def __init__(self) -> None:
        self._left = None
        self._right = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, edge: Edge):
        self._left = edge

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, edge: Edge):
        self._right = edge



class DrawNode:

    def __init__(self, node: TreeNode, position=60, level = 0, adjust_position = True) -> None:
        self.node = node
        self._position = position
        self.level = level

        self.offset = 0

        self.left = None
        self.right = None
        self.width = len(node)
        self.value_width = len(str(node.value))
        self.left_width = 0
        self.right_width = 0

        self.edges = Edges()

        if node.left is not None:
            self.edges.left = Edge(EdgeDirection.LEFT, self.get_base_edge_position_left())
            self.left = DrawNode(node.left, self.left_child_position, level + 1, False)
            self.width += self.left.width
            self.left_width = self.left.width

            displacement = min(self.pivot - PIVOT_MARGIN + 1 - self.left.right_boundary, 0)
            self.left.move(displacement)
            self.edges.left.move(displacement)

        if node.right is not None:
            self.edges.right = Edge(EdgeDirection.RIGHT, self.get_base_edge_position_right())
            self.right = DrawNode(node.right, self.right_child_position, level + 1, False)
            self.width += self.right.width
            self.right_width = self.right.width

            displacement = max(self.pivot - self.value_width % 2 + PIVOT_MARGIN - self.right.left_boundary  , 0)
            self.right.move(displacement)
            self.edges.right.move(displacement)


        if adjust_position:
            self.move(max(self.left_boundary - LEFT_MARGIN, 0) * -1)


    @property
    def extension_left(self):
        if self.edges.left:
            return max(self.position - self.edges.left.position - 1, 0)
        return 0

    @property
    def extension_right(self):
        if self.edges.right:
            return max( self.edges.right.position - (self.position + len(self.node))  , 0)
        return 0


    @property
    def position(self):
        return self.offset + self._position

    @property
    def extended_position(self):
        return self.position - self.extension_left



    @position.setter
    def set_position(self, position):
        self._position = position

    def move(self, offset):
        if offset == 0:
            return
        self.offset += offset
        if self.edges.left:
            self.edges.left.move(offset)
        if self.edges.right:
            self.edges.right.move(offset)
        if self.left:
            self.left.move(offset)
        if self.right:
            self.right.move(offset)

    @property
    def left_boundary(self):
        if self.left:
            return min(self.position - self.extension_left, self.left.left_boundary)
        return self.position - self.extension_left

    @property
    def right_boundary(self):
        if self.right:
            return max(self.position + len(self.node) + self.extension_right, self.right.right_boundary)
        return self.position + len(self.node) + self.extension_right

    @property
    def pivot(self):
        return self.position + max(self.value_width // 2 - 1 , 0)

    @property
    def left_child_position(self):
        if not self.edges.left or not self.node.left:
            raise ValueError("There is no left child node")
        return self.offset + self.edges.left.position - len(self.node.left) % 2  - max(len(self.node.left) // 2 , 0)

    @property
    def right_child_position(self):
        if not self.edges.right or not self.node.right:
            raise ValueError("There is no left child node")
        return self.offset + self.edges.right.position + 1  - max(len(self.node.right) // 2 , 0)

    def get_base_edge_position_right(self):
        return self.offset +  self.pivot + 1 if len(self) % 2 == 1 else self.pivot + 2

    def get_base_edge_position_left(self):
        return self.offset + self.pivot - 1




    def get_left_child_position(self, value_length, edge_position):
        if value_length % 2 == 1:
            return edge_position - 1 - (value_length // 2)

        return  edge_position - (value_length // 2)


    def get_right_child_position(self, value_length, edge_position):
        if value_length % 2 == 1:
            return edge_position + 1 - (value_length // 2)
        return edge_position - value_length // 2

    def __str__(self):
        return "_" * self.extension_left + f"{self.node.value}" + "_" * self.extension_right

    def __repr__(self) -> str:
        return f"Node: {self.node.value} position {self.position}"

    def __len__(self):
        return len(str(self))

    def walk(self):
        # print(f'\nNode {self}')
        # print(f'  width: {self.width}')
        # print(f'  left_width: {self.left_width}')
        # print(f'  right_width: {self.right_width}')

        if self.left:
            self.left.walk()

        if self.right:
            self.right.walk()




def build_levels(root: DrawNode):
    result = []

    queue = [root]

    while len(queue) > 0:
        node = queue.pop(0)


        if len(result) - 1 < node.level:
            result.append([])

        result[node.level].append(node)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result

def draw(root: DrawNode):

    levels = build_levels(root)
    for level in levels:
        line = ""
        position = 0
        for node in level:
            line += " " * (node.extended_position - position)
            line += str(node)
            position = node.extended_position + len(node)

        print(line)

        edge_line = ""
        edge_position = 0
        for node in level:
            left = node.edges.left
            right = node.edges.right
            if left:
                edge_line += " " * (left.position - edge_position)
                edge_line += str(left)
                edge_position = (left.position +1)


            if right:
                edge_line += " " * (right.position - edge_position)
                edge_line += str(right)
                edge_position = (right.position +1)

        print(edge_line)


    


def main():
    root = TreeNode(144, TreeNode(2, TreeNode(6, TreeNode(7)), TreeNode(1, None, TreeNode(9, None, TreeNode(22)))), TreeNode(5, TreeNode(1, TreeNode(9, TreeNode(23234234232, TreeNode(3), TreeNode(2)), TreeNode(234234)), TreeNode(323423423423445345)), TreeNode(13, TreeNode(4), TreeNode(8))))
    wrapped = DrawNode(root)
    draw(wrapped)

    # root = TreeNode(1, TreeNode(1234, TreeNode(123, TreeNode(23413)) ), TreeNode(129, TreeNode(32, TreeNode(3, TreeNode(5))), TreeNode(234)))
    # root = TreeNode(89, TreeNode(1, TreeNode(4), TreeNode(3)), TreeNode(332332, None, TreeNode(9, None, TreeNode(1))))


    # wrapped = DrawNode(root, 40)
    # wrapped.walk()
    # draw(wrapped)

    root = TreeNode(92938479283749827834, TreeNode(3), TreeNode(14))
    wrapped = DrawNode(root,  99)
    draw(wrapped)

    root = TreeNode(92, TreeNode(3), TreeNode(14))
    wrapped = DrawNode(root)
    draw(wrapped)

    root = TreeNode(2, TreeNode(3), TreeNode(14))
    wrapped = DrawNode(root)
    draw(wrapped)
if __name__ == "__main__":
    main()

main()
