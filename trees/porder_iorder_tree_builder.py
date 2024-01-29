from TreeNode import *
from visualize_tree import visualize_tree

def build_tree_helper(p_order, i_order, left, right, mapping, p_index):
    if left > right:
        return None
    current_node_data = p_order[p_index[0]]
    p_index[0] += 1
    root = TreeNode(current_node_data)

    if left == right:
        return root
    
    in_index = mapping[current_node_data]
    root.left = build_tree_helper(p_order, i_order, left, in_index - 1, mapping, p_index)
    root.right = build_tree_helper(p_order, i_order, in_index + 1, right, mapping, p_index)
    return root

def build_tree(p_order, i_order):
    mapping = {}
    for idx in range(len(i_order)):
        mapping[i_order[idx]] = idx 
    p_index = [0]
    return build_tree_helper(p_order, i_order, 0, len(p_order) - 1, mapping, p_index)


def main():
    
    p_order = [
        [3, 9, 20, 15, 7],
        [-1],
        [10, 20, 40, 50, 30, 60],
        [1, 2, 4, 5, 3, 6],
        [1, 2, 4, 7, 3],
        [1, 2, 4, 8, 9, 5, 3, 6, 7]
        
    ]
    
    i_order = [
        [9, 3, 15, 20, 7],
        [-1],
        [40, 20, 50, 10, 60, 30],
        [4, 2, 5, 1, 6, 3],
        [4, 2, 7, 1, 3],
        [8, 4, 9, 2, 5, 1, 6, 3, 7]
    ]
    
    indx = 0
    for i in range(len(p_order)):
        tr = build_tree(p_order[indx], i_order[indx])
        visualize_tree(tr)
        #print(viz)
        indx += 1

        

if __name__ == '__main__':
    main()