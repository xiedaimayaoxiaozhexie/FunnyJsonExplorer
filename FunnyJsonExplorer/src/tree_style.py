from drawable import Container, Leaf

class TreeContainer(Container):
    def draw(self, indent=""):
        print(f"{indent}├─ {self.icon} {self.name}")
        for i, child in enumerate(self.children):
            next_indent = indent + "│  " if i < len(self.children) - 1 else indent + "   "
            child.draw(next_indent)

class TreeLeaf(Leaf):
    def draw(self, indent=""):
        print(f"{indent}└─ {self.icon} {self.name}")

class TreeStyleFactory:
    def __init__(self, icon):
        self.icon = icon

    def create_container(self, name, level):
        return TreeContainer(self.icon, name, level)

    def create_leaf(self, name):
        return TreeLeaf(self.icon, name)
