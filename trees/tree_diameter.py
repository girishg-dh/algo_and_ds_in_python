from TreeNode import *
from BinaryTree import *


def diameter_helper(node: TreeNode, diameter: int):
    if node is None:
        return 0, diameter
    else:
        left, diameter = diameter_helper(node.left, diameter)
        right, diameter = diameter_helper(node.right, diameter)
        diameter = max(diameter, left + right)
        return max(left, right) + 1, diameter

def diameter_of_binaryTree(root):
    diameter = 0
    if not root:
        return 0

    _, diameter = diameter_helper(root, diameter)

    return diameter

def main():
    list_of_trees = [ [TreeNode(2), TreeNode(1), TreeNode(4), TreeNode(3), TreeNode(5), TreeNode(6), TreeNode(7)],
                    [TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)],
                    [TreeNode(45), TreeNode(32), TreeNode(23), TreeNode(21), TreeNode(18), TreeNode(1)],
                    [TreeNode(5), TreeNode(3), TreeNode(4), TreeNode(1), TreeNode(2), TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)],
                    [TreeNode(-1), TreeNode(-5), TreeNode(-8), TreeNode(-3), TreeNode(1), TreeNode(5), TreeNode(3)],
                    [TreeNode(9), TreeNode(7), None, None, TreeNode(1), TreeNode(8), TreeNode(10), None, TreeNode(12)]
    ]
    for tree in list_of_trees:
        bTree = BinaryTree(tree)
        print(diameter_of_binaryTree(bTree.root))

if __name__ == '__main__':
    main()