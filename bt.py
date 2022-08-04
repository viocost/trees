class TreeNode:
    def __init__(self, value, left=None, right=None, color=None) -> None:
        self._value = value
        self.left = left
        self.right = right
        self.color = color

    def __repr__(self) -> str:
        return self._value

    def __str__(self) -> str:
        return self._value

    def __len__(self):
        return len(self.__str__())

    def __eq__(self, other) -> bool:
        return self._value == other._value

    def __gt__(self, other) -> bool:
        return self._value > other._value

    def __lt__(self, other) -> bool:
        return self._value < other._value

    def __ge__(self, other) -> bool:
        return self._value >= other._value

    def __le__(self, other) -> bool:
        return self._value <= other._value

    def clone(self):
        root = self.__class__(self._value, color=self.color)
        if self.left:
            root.left = self.left.clone()
        if self.right:
            root.right = self.right.clone()

        return root



