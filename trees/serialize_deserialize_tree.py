from TreeNode import *
from BinaryTree import *

##from ds_v1.BinaryTree.BinaryTree import TreeNode
m = 1
def recurrsive_serialize(node: TreeNode, serialized_list: list):
    global m

    if node is None:
        serialized_list.append("N{}".format(m))
        m += 1
        return
    serialized_list.append(node.data)
    recurrsive_serialize(node.left, serialized_list)
    recurrsive_serialize(node.right, serialized_list)

def recurrsive_deserialize(serialized_list: list) -> TreeNode:
    value = serialized_list.pop()
    if type(value) == str and value[0] == "N":
        return None
    node = TreeNode(value)
    node.left = recurrsive_deserialize(serialized_list)
    node.right = recurrsive_deserialize(serialized_list)
    return node

def serialize(root: TreeNode):
    serialized_list = []
    recurrsive_serialize(root, serialized_list)
    return serialized_list

def deserialize(stream: list) -> TreeNode:
    stream.reverse()
    node = recurrsive_deserialize(stream)
    return node


def main():
    global m
    input_trees = [
        [TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(75), TreeNode(350)],
        [TreeNode(100), TreeNode(200), TreeNode(75), TreeNode(50), TreeNode(25), TreeNode(350)],
        [TreeNode(200), TreeNode(350), TreeNode(100), TreeNode(75), TreeNode(50), TreeNode(200), TreeNode(25)],
        [TreeNode(25), TreeNode(50), TreeNode(75), TreeNode(100), TreeNode(200), TreeNode(350)],
        [TreeNode(350), TreeNode(75), TreeNode(25), TreeNode(200), TreeNode(50), TreeNode(100)],
        [TreeNode(1), None, TreeNode(2), None, TreeNode(3), None, TreeNode(4), None, TreeNode(5)]
    ]

    indx = 1
    for i in input_trees:
        tree = BinaryTree(i)

        # Serialization
        ostream = serialize(tree.root)
        print("\n\tSerialized integer list:")
        print("\t" + str(ostream))

        # Deserialization
        deserialized_root = deserialize(ostream)
        m = 1

if __name__ == '__main__':
    main()