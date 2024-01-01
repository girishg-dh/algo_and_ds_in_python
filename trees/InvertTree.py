from TreeNode import *
from BinaryTree import *

def mirror_binary_tree(root: TreeNode):
    if not root:
        return None
    if root.left:
        mirror_binary_tree(root.left)
    if root.right:
        mirror_binary_tree(root.right)
    root.left, root.right = root.right, root.left
    return root



if __name__ == "__main__":
    input_trees = [
        [TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(75), TreeNode(125), TreeNode(350)],
        [TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(110), TreeNode(125), TreeNode(350)],
        [TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(75), TreeNode(90), TreeNode(350)],
        [TreeNode(25), TreeNode(50), TreeNode(75), TreeNode(100), TreeNode(125), TreeNode(350)],
        [TreeNode(350), TreeNode(125), TreeNode(100), TreeNode(75), TreeNode(50), TreeNode(25)],
        [TreeNode(100)],
        [TreeNode(1), TreeNode(2), None, TreeNode(3), None, TreeNode(4)],
        [TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), None, None, TreeNode(5)],
        []
    ]
    for indx in range(len(input_trees)):
        tree = BinaryTree(input_trees[indx])
        solution = mirror_binary_tree(tree.root)


