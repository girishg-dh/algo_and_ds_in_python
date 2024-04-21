from node import Node
from graph_utility import *

def clone(root):
    """
    This function clones a graph by creating a new node for each node in the original graph.

    Parameters:
        root (Node): The root node of the original graph.

    Returns:
        Node: The root node of the cloned graph.
    """
    visited_nodes = dict()
    return clone_recursive(root, visited_nodes)

def clone_recursive(root, visited_nodes):
    """
    This function clones a graph recursively by creating a new node for each node in the original graph.

    Parameters:
        root (Node): The root node of the original graph.

    Returns:
        Node: The root node of the cloned graph.
    """
    if root is None:
        return None
    cloned_node = Node(root.data)
    visited_nodes[root] = cloned_node
    for neighbour in root.neighbours:
        if neighbour in visited_nodes:
            cloned_node.neighbours.append(visited_nodes[neighbour])
        else:
            cloned_node.neighbours.append(clone_recursive(neighbour, visited_nodes))
    return cloned_node

# Driver codedef main():
def main():
    """
    This function is the main entry point of the program. It creates a list of graphs and performs operations on each graph.
    
    Parameters:
        None
    
    Returns:
        None
    """
    data = [[[2, 3], [1, 3], [1, 2]],
            [[2, 4], [1, 3], [2, 4], [1, 3]],
            [[2, 5], [1, 3], [2, 4], [3, 5], [1, 4]],
            [[2], [1]],
            [[2, 6], [1, 3], [2, 4], [3, 5], [4, 6], [1, 5]],
            [[]]
            ]

    for i in range (len(data)):
      node1 = create_graph(data[i])
      print(i+1, ".\t Original Graph: ", create_2D_list(node1), "\n", sep="")
      print_graph(node1)
      print()
      cloned_root = clone(node1)
      print("\t Cloned Graph: ", create_2D_list(cloned_root), "\n", sep="")
      print_graph(node1)
      print("-"*100)  

if __name__ == '__main__':
    main()