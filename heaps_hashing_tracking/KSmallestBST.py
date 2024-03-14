'''Statement: Given the root node of a binary search tree and an integer value k, return the k-th smallest value in the tree.'''

from BinaryTree import *
from TreeNode import TreeNode
import heapq

def kth_smallest_element(root, k):
    result = []
    result = kth_smallest_element_rec(root, result)
    for i in range(k-1):
        heapq.heappop(result)
    val, _ = heapq.heappop(result)
    return val



def kth_smallest_element_rec(root: TreeNode, result):
    if root.left:
        result = kth_smallest_element_rec(root.left, result)
    if root:
        heapq.heappush(result, (root.data, root))
    else:
        return result

    if root.right:
        result = kth_smallest_element_rec(root.right, result)
    
    return result
    






def main():
    list_of_trees = [ [TreeNode(6), TreeNode(2), TreeNode(8), TreeNode(0), TreeNode(4), TreeNode(7), TreeNode(9), None, None, TreeNode(3), TreeNode(5)],
                      [TreeNode(6), TreeNode(2), TreeNode(8), TreeNode(0), TreeNode(4), TreeNode(7), TreeNode(9), None, None, TreeNode(3), TreeNode(5)],
                      [TreeNode(2), TreeNode(1)],
                      [TreeNode(5), TreeNode(3), TreeNode(9), TreeNode(1), TreeNode(2), TreeNode(7), TreeNode(10), None, None, None, None, TreeNode(6), TreeNode(8)],
                      [TreeNode(100), TreeNode(88), TreeNode(130)]
                    ]
    list_of_k = [2, 4, 1, 6, 3]

    input_trees = []
    for list_of_nodes in list_of_trees:
        tree = BinaryTree(list_of_nodes)
        input_trees.append(tree)

    x = 1
    for tree in input_trees:
        print(x,".\tk = ", list_of_k[x-1], sep = "")
        print("\n\tkth smallest element: ", kth_smallest_element(tree.root,list_of_k[x-1]), sep = "")
        x += 1
        print("-" * 100)
    
if __name__ == '__main__':
    main()