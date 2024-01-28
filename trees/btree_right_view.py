from BinaryTree import TreeNode
import tree_helper

def right_side_view(root):
    result = []
    if root is None:
        return []
    
    return []


def dfs(root, rside, level):
    if len(rside) == level:
        rside.append(root.data)
        level += 1



def main():
    node_list = [1,2,3,None,None,4,5]
    tree = tree_helper.createTree(node_list)
    print(right_side_view(tree.root))


if __name__ == "__main__":
    main()