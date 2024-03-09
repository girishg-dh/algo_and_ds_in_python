from anyio import current_effective_deadline
from TreeNode import TreeNode
from BinaryTree import *
from collections import deque

def printing_queue(current):
    if current:
        output = "["
        for x in current:
            output += str(x.data) + ", "
        output = output[:-2] + "]"
        return output
    return "[]"

def level_order_traversal(root):
    current_queue, next_queue = deque(), deque()
    result = ""
    if not root:
        return "None"
    current_queue.append(root)
    while len(current_queue) > 0:
        root = current_queue.popleft()
        result = result + str(root.data) + ", "
        if root.left:
            next_queue.append(root.left)
        if root.right:
            next_queue.append(root.right)
        if len(current_queue) == 0 and len(next_queue) > 0:
                result = result[:-2] + " : "
                current_queue = next_queue
                next_queue = deque()
    return result[:-2]


def main():
    test_cases_roots = []

    input1 = [
        TreeNode(100),
        TreeNode(50),
        TreeNode(200),
        TreeNode(25),
        TreeNode(75),
        TreeNode(350)
    ]
    tree1 = BinaryTree(input1)
    test_cases_roots.append(tree1.root)

    input2 = [
        TreeNode(25),
        TreeNode(50),
        None,
        TreeNode(100),
        TreeNode(200),
        TreeNode(350)
    ]
    tree2 = BinaryTree(input2)
    test_cases_roots.append(tree2.root)

    input3 = [
        TreeNode(350),
        None,
        TreeNode(100),
        None,
        TreeNode(50),
        TreeNode(25)
    ]
    tree3 = BinaryTree(input3)
    test_cases_roots.append(tree3.root)

    tree4 = BinaryTree([TreeNode(100)])
    test_cases_roots.append(tree4.root)

    test_cases_roots.append(None)

    for i in range(len(test_cases_roots)):
        if i > 0:
            print()
        print(i + 1, ".\tBinary Tree")
        print("\n\tLevel order traversal: ")
        print("\t",level_order_traversal(test_cases_roots[i]))
        print("\n" + '-' * 100)


if __name__ == '__main__':
    main()
        
