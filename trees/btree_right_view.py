from BinaryTree import TreeNode
import tree_helper

def right_side_view(root):
    if root is None:
        return []
    rside = []
    dfs(root, rside, 0)
    return rside

def dfs(root, rside, level):
    if len(rside) == level:
        rside.append(root.data)
    if root.right is not None:
        dfs(root.right, rside, level+1)
    if root.left is not None:
        dfs(root.left, rside, level+1)

def main():
    node_list = [1,2,3,None,None,4,5]
    node_list2 = [1,2,3,4,5,6,7,8]
    tree = tree_helper.createTree(node_list)
    tree2 = tree_helper.createTree(node_list2)
    print(right_side_view(tree.root))
    print(right_side_view(tree2.root))


if __name__ == "__main__":
    main()