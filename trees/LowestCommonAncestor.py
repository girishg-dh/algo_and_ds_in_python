# Statement
# Given a binary search tree with n
# nodes, your task is to find the lowest common ancestor of two of its nodes, node1 and node2.
# The lowest common ancestor of two nodes, node1 and node2, is defined as the lowest node 
#in the binary search tree that has both node1 and node2 as descendants.
# By definition, a node is a descendant of itself. 
#For example, if node2 is a descendant of node1, and we know that node1 is a descendant of itself, 
#then node1 will be the lowest common ancestor of node1 and node2.

from BinaryTree import *
from TreeNode import *
from visualize_tree import visualize_tree
from tree_helper import createTree

def lowest_common_ancestor(root, node1, node2):
    ancestor = root
    if node1.data < root.data and node2.data < root.data:
        ancestor = lowest_common_ancestor(root.left, node1, node2)
    if node1.data > root.data and node2.data > root.data:
        ancestor = lowest_common_ancestor(root.right, node1, node2)
    return ancestor

def main():
    tree = createTree([20, 8, 22, 4, 12, None, None, None, None, 10, 14])
    n1, n2 = TreeNode(10) , TreeNode(14)
    result = lowest_common_ancestor(tree.root, n1, n2)
    print(result.data)
if __name__=="__main__":
    main()
