import argparse
from explorer import FunnyJsonExplorer
from tree_style import TreeStyleFactory
from rectangle_style import RectangleStyleFactory
from icon_mapping import ICON_MAP

def main():
    parser = argparse.ArgumentParser(description="Funny JSON Explorer")
    parser.add_argument("-f", "--file", required=True, help="Path to JSON file")
    parser.add_argument("-s", "--style", required=True, choices=["tree", "rectangle"], help="Display style")
    parser.add_argument("-i", "--icon", required=False, help="Icon type", choices=ICON_MAP.keys())

    args = parser.parse_args()

    icon = ICON_MAP.get(args.icon, "")

    if args.style == "tree":
        style_factory = TreeStyleFactory(icon)
    elif args.style == "rectangle":
        style_factory = RectangleStyleFactory(icon)

    explorer = FunnyJsonExplorer()
    explorer.load(args.file, style_factory)
    explorer.show()

if __name__ == "__main__":
    main()
