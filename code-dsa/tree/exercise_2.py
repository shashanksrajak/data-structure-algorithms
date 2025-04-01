# Question Link
# https: //github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md


# ------

class Tree_node:

    # This creates a node with data {name, designation}
    def __init__(self, name, designation):
        self.data = {"name": name, "designation": designation}
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

    # recursive function to print the tree
    def print_tree(self, level):
        current_level = self.get_level()

        if current_level > level:
            return

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + f"{self.data["name"]} ({self.data["designation"]})")

        if self.children:
            for child in self.children:
                child.print_tree(level)


def build_management_tree():

    root = Tree_node("Nilupul", "CEO")

    cto = Tree_node("Chinmay", "CTO")
    infra_head = Tree_node("Vishwa", "Infrastructure Head")
    cto.add_child(infra_head)
    infra_head.add_child(Tree_node("Dhaval", "Cloud Manager"))
    infra_head.add_child(Tree_node("Abhijit", "App Manager"))
    cto.add_child(Tree_node("Aamire", "Application Head"))

    hr_head = Tree_node("Gels", "HR Head")
    hr_head.add_child(Tree_node("Peter", "Recruitment Manager"))
    hr_head.add_child(Tree_node("Waqas", "Policy Manager"))

    root.add_child(cto)
    root.add_child(hr_head)

    root.print_tree(3)


if __name__ == "__main__":
    build_management_tree()
