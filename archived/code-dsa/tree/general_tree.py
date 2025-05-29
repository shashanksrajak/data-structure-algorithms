class Tree_node:

    # This creates a node
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        cursor = self.parent
        level = 0
        while cursor:
            level = level+1
            cursor = cursor.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = Tree_node("Electronics")

    laptop = Tree_node("Laptop")
    laptop.add_child(Tree_node("Macbook"))
    laptop.add_child(Tree_node("Surface"))
    laptop.add_child(Tree_node("Delll"))

    mobile = Tree_node("mobile")
    mobile.add_child(Tree_node("Nokia"))
    mobile.add_child(Tree_node("iPhone"))
    mobile.add_child(Tree_node("Xiamoi"))

    tv = Tree_node("TV")
    tv.add_child(Tree_node("Sony"))
    tv.add_child(Tree_node("LG"))
    tv.add_child(Tree_node("Samsung"))

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)

    root.print_tree()


if __name__ == "__main__":
    build_product_tree()
