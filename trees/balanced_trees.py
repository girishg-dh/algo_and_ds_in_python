from TreeNode import *
from BinaryTree import *

def is_balanced(root: TreeNode) -> bool:
    return recurrsive_height(root) != -1



def recurrsive_height(node: TreeNode):
    if node is None:
        return 0

    left_height = recurrsive_height(node.left)
    if left_height == -1:
        return -1

    right_height = recurrsive_height(node.right)
    if right_height == -1:
        return -1

    if abs(right_height - left_height) > 1:
        return -1

    return max(right_height, left_height) + 1




input_trees = [[TreeNode(6), TreeNode(2), TreeNode(8), TreeNode(0), TreeNode(4), TreeNode(7), TreeNode(9), None, None, TreeNode(3), TreeNode(5)],
        [TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), None, TreeNode(6), TreeNode(7), TreeNode(8), None, TreeNode(9), None, TreeNode(10)],
        [TreeNode(5), TreeNode(3), TreeNode(9), TreeNode(1), TreeNode(2), TreeNode(7), TreeNode(10), None, None, None, None, TreeNode(6), TreeNode(8)],
        [TreeNode(100), TreeNode(88), None, TreeNode(10)],
        [TreeNode(1), None, TreeNode(2), None, TreeNode(3), None, TreeNode(4), None, TreeNode(5), None, TreeNode(6)]]

for tree in input_trees:
    bTree = BinaryTree(tree)
    print(is_balanced(bTree.root))