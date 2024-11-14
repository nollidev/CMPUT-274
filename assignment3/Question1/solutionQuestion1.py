# Name: Nathan Edillon
# ccid: nedillon
# studentId: 1826864 
# operating system: Fedora Linux 41 
# python version: 3.12.6
from treenode import TreeNode

def construct_tree(length_of_tree, max_children, iterable, iteration=0, root=None): 
    while iteration < length_of_tree:
        if root == None:
            root = TreeNode(next(iterable)); iteration += 1; continue
        elif len(root.get_children()) != max_children:
            root.add_child(TreeNode(next(iterable))); iteration += 1; continue
        else:
            for child in root.get_children():
                construct_tree(length_of_tree, max_children, iterable, iteration, child)
    return root

def read_tree():
    """Construct a tree from standard input

    The first line of standard input will have the format: n d
        - n: The length of the array-based representation of the tree
        - d: The maximum number of children a node can have

    The second line contains n space-separated strings where each string
    represents the value of a TreeNode. A string can be a single character
    (eg. 'W') or a series of characters (eg. 'AA', 'AB'). The dash '-' character
    represents an empty node and should be ignored.

    Returns:
        The root of the tree as a TreeNode object
    """
    # TODO: Write your code for read_tree() here!
    tree_criteria = input().split()
    length_of_tree, max_nodes = tree_criteria[0], tree_criteria[1]
    tree_array = input().split()
    # print(tree_array)
    return construct_tree(length_of_tree, max_children, iter(tree_array))

def main():
    # Do not modify
    read_tree().print_tree()


if __name__ == "__main__":
    main()
