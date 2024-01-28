from TreeNode import *
from BinaryTree import *
from collections import deque
node_list = deque()

def find_max_depth(root: TreeNode) -> int:
    global node_list
    if not root:
        return node_list.maxlen
    if root.left:

    return 0 
