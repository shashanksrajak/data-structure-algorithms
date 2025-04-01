# Question Link
# https: //github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md


# ------

class TreeNode:

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

    def print_tree(self, mode=None):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        if mode == "name":
            print(prefix + self.data["name"])
        elif mode == "designation":
            print(prefix + self.data["designation"])
        else:
            print(prefix + f"{self.data['name']} ({self.data['designation']})")

        if self.children:
            for child in self.children:
                child.print_tree(mode)


def build_management_tree():

    root = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinmay", "CTO")
    infra_head = TreeNode("Vishwa", "Infrastructure Head")
    cto.add_child(infra_head)
    infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))
    cto.add_child(TreeNode("Aamire", "Application Head"))

    hr_head = TreeNode("Gels", "HR Head")
    hr_head.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    root.add_child(cto)
    root.add_child(hr_head)

    root.print_tree("both")


if __name__ == "__main__":
    build_management_tree()
