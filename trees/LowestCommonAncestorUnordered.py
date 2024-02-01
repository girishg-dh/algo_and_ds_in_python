from TreeNode import *
from tree_helper import createTree
from BinaryTree import TreeNode


class Solution:
    lca: TreeNode
    def __init__(self) -> None:
        self.lca = None
    def lowest_common_ancestor(self, root, p, q):
        self.lowest_common_ancestor_recursive(root, p , q)
        return self.lca

    def lowest_common_ancestor_recursive(self, current_node: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        if not current_node:
            return False
        left, mid, right = False, False, False
        if current_node.data == p.data or current_node.data == q.data:
            mid = True
        left = self.lowest_common_ancestor_recursive(current_node.left, p, q)
        if not self.lca:
            right = self.lowest_common_ancestor_recursive(current_node.right, p, q)

        if left + right + mid >= 2:
            self.lca = current_node
        return mid or left or right



if __name__=="__main__":
    tree = createTree([3, 9, 20, 15, 7])
    p, q = TreeNode(3), TreeNode(9)
    solution: TreeNode = Solution().lowest_common_ancestor(tree.root, p, q)
    print(solution.data)