from abc import ABC, abstractmethod
from drawable import Container, Leaf

class IconFactory(ABC):
    @abstractmethod
    def get_icon(self):
        pass

class CircleIconFactory(IconFactory):
    def get_icon(self):
        return "◯"

class SquareIconFactory(IconFactory):
    def get_icon(self):
        return "■"

class TreeStyleFactory:
    def __init__(self, icon):
        self.icon = icon

    def create_container(self, name, level):
        return Container(self.icon, name, level)

    def create_leaf(self, name):
        return Leaf(self.icon, name)

class RectangleStyleFactory:
    def __init__(self, icon):
        self.icon = icon

    def create_container(self, name, level):
        return Container(self.icon, name, level)

    def create_leaf(self, name):
        return Leaf(self.icon, name)
