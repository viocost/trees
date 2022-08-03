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
