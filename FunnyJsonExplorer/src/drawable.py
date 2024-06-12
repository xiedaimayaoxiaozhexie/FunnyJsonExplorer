from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self, indent=""):
        pass

class Container(Drawable):
    def __init__(self, icon, name, level=0):
        self.icon = icon
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def draw(self, indent=""):
        print(f"{indent}{self.icon} {self.name}")
        for child in self.children:
            child.draw(indent + "│  ")

class Leaf(Drawable):
    def __init__(self, icon, name):
        self.icon = icon
        self.name = name

    def draw(self, indent=""):
        print(f"{indent}└─ {self.icon} {self.name}")
