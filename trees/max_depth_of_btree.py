from TreeNode import *
from BinaryTree import *
#from collections import deque
#node_list = deque()

def find_max_depth_v1(root: TreeNode) -> int:
    if root is None:
        return 0
    return max(find_max_depth_v1(root.left), find_max_depth_v1(root.right)) + 1

def find_max_depth(root):
    if root is None:
        return 0 
    node_stack = deque([(root, 1)])
    max_depth = 0

    while node_stack:
        root, depth = node_stack.pop()
        if root.left:
            node_stack.append((root.left, depth + 1))
        if root.right:
            node_stack.append((root.right, depth + 1))
        if root.right is None and root.right is None:
            max_depth = max(max_depth, depth)
    return max_depth
