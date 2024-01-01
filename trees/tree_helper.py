from TreeNode import *
from typing import List

class TreeHelper:
    def __init__(self, node_list) -> None:
        self.tree_nodes = self.createTrees(self, node_list)

    def createTrees(self, node_list: List):
        tree_nodes = []
        for node in node_list:
            tree_nodes.append(TreeNode(node))
        return tree_nodes

