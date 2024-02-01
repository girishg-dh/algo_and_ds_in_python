from TreeNode import *
from BinaryTree import *
from typing import List


def createTree(node_list: List)->BinaryTree:
    tree_nodes = []
    for node in node_list:
        if node is not None:
            tree_nodes.append(TreeNode(node))
        else:
            tree_nodes.append(None)
    return createNodeTree(tree_nodes)

def createNodeTree(node_list: List[TreeNode]) -> BinaryTree:
    return BinaryTree(node_list)


