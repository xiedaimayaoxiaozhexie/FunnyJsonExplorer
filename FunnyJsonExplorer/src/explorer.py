import json

class FunnyJsonExplorer:
    def load(self, file_path, style_factory):
        with open(file_path, 'r') as file:
            data = json.load(file)
        self.root = self._build_tree(data, style_factory)

    def _build_tree(self, data, style_factory, level=0):
        if isinstance(data, dict):
            container = style_factory.create_container("root", level)
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    child = self._build_tree(value, style_factory, level + 1)
                    child.name = key  # 设置子节点名称
                else:
                    child = style_factory.create_leaf(f"{key}: {value}")
                container.add(child)
            return container
        else:
            return style_factory.create_leaf(str(data))

    def show(self):
        self.root.draw()
