from node import *

def create_graph( data ):
    """
    Creates a graph based on the input data array.

    Parameters:
    data (list): The input data array containing the adjacency information.

    Returns:
    Node: The starting node of the created graph.
    """
    if len(data) == 0:
        return Node(1)
    nodes = []

    for i in range(len(data)):
        nodes.append(Node(i+1))

    for i, node in enumerate(nodes):
        for neighbor in data[i]:
            node.neighbors.append(nodes[neighbor-1])
    return nodes[0]

def create_2D_list(root):
    """
    A function to create a 2D list based on the input node data and its neighbors.

    Parameters:
    root (Node): The root node of the graph.

    Returns:
    list: A 2D list representing the graph based on the adjacency information.
    """
    if root is None:
        return []
    queue = [root]
    visited =  {}
    graph = []
    node_index = {}

    while queue:
        node = queue.pop(0)
        neighbours = []
        for neighbor in node.neighbors:
            neighbours.append(visited.get(neighbor, neighbor).data)
            if neighbor not in visited and neighbor not in queue:
                visited[neighbor] = neighbor
                queue.append(neighbor)
        neighbours.sort()
        if node not in node_index:
            node_index[node] = len(graph)
            graph.append([node.data, neighbours])
        else:
            graph[node_index[node]][1] = neighbours
    graph.sort(key=lambda x: x[0])
    return [sublist[1] for sublist in graph]

def print_graph_rec(root, visited_nodes):
    """
    Recursively prints the graph starting from the given root node.

    Parameters:
        root (Node): The root node of the graph.
        visited_nodes (set): A set of visited nodes to avoid cycles.

    Returns:
        None
    """
    if root is None or root in visited_nodes:
        return
    visited_nodes.add(root)
    print("\t", root.data, end=": { ")
    for n in root.neighbors:
        print(str(n.data), end=" ")
    print("}")
    for n in root.neighbors:
        print_graph_rec(n, visited_nodes)

def print_graph(root):
    """
    Recursively prints the graph starting from the given root node.

    Parameters:
        root (Node): The root node of the graph.

    Returns:
        None
    """
    visited_nodes = set()
    print_graph_rec(root, visited_nodes)