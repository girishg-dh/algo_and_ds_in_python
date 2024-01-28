from TreeNode import *
from BinaryTree import *
from typing import List


def createTree(node_list: List):
    tree_nodes = []
    for node in node_list:
        if node is not None:
            tree_nodes.append(TreeNode(node))
        else:
            tree_nodes.append(None)
    return createNodeTree(node_list)

def createNodeTree(node_list):
    return BinaryTree(node_list)


