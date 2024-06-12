from drawable import Container, Leaf

class RectangleContainer(Container):
    def draw(self, indent=""):
        print(f"{indent}┌─ {self.icon}{self.name}{'─' * (35 - len(self.name))}┐")
        for child in self.children:
            child.draw(indent + "│  ")
        print(f"{indent}└{'─' * 38}┘")

class RectangleLeaf(Leaf):
    def draw(self, indent=""):
        print(f"{indent}├─ {self.icon}{self.name}{'─' * (35 - len(self.name))}┤")

class RectangleStyleFactory:
    def __init__(self, icon):
        self.icon = icon

    def create_container(self, name, level):
        return RectangleContainer(self.icon, name, level)

    def create_leaf(self, name):
        return RectangleLeaf(self.icon, name)
