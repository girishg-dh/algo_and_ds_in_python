from TreeNode import *
from BinaryTree import *
import tree_helper
import math

def validate_bst_rec(current_node: TreeNode, prev):
    if not current_node:
        return True
    if not validate_bst_rec(current_node.left, prev):
        return False
    if current_node.data <= prev[0]:
        return False
    prev[0] = current_node.data
    return validate_bst_rec(current_node.right, prev)

def validate_bst(root: TreeNode):
    prev = [-math.inf]
    return validate_bst_rec(root, prev)