# Name: Nathan Edillon
# ccid: nedillon
# studentId: 1826864 
# operating system: Fedora Linux 41 
# python version: 3.13.0
from treenode import TreeNode

def construct_tree(max_children, node, root): 
    if root == None:
        root = TreeNode(node)
    elif len(root.get_children()) == int(max_children):
        return root
        # child = construct_tree(max_children, node, child)
    else:
        root.add_child(TreeNode(node))
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
    root = None
    for node in tree_array:
        root = construct_tree(max_nodes, node, root)
    return root

def main():
    # Do not modify
    read_tree().print_tree()


if __name__ == "__main__":
    main()
