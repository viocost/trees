class TreeNode:
    def __init__(self, value, left=None, right=None, color=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.color = color

    def __repr__(self) -> str:
        return str(self.value)

    def __str__(self) -> str:
        return str(self.value)

    def __len__(self):
        return len(self.__str__())

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __gt__(self, other) -> bool:
        return self.value > other.value

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __ge__(self, other) -> bool:
        return self.value >= other.value

    def __le__(self, other) -> bool:
        return self.value <= other.value

    def clone(self):
        root = TreeNode(self.value, color=self.color)
        if self.left:
            root.left = self.left.clone()
        if self.right:
            root.right = self.right.clone()

        return root



