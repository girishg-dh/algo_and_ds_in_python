def create_adjacency_list(n:int, edges:list):
    adj = [set() for _ in range(n)]

    for v1, v2 in edges:
        adj[v1].add(v2)
        adj[v2].add(v1)
    return adj

def min_height_trees(n, edges):
    if n <= 2:
        return [i for i in edges]

    adj = create_adjacency_list(n, edges)

    leaves = [i for i in range(n) if len(adj[i]) == 1]

    remaining_nodes = n

    while remaining_nodes > 2:
        remaining_nodes -= len(leaves)
        next_leaves = []

        while leaves:
            current_leaf = leaves.pop()
            neighbour = adj[current_leaf].pop()
            adj[neighbour].remove(current_leaf)

            #if after removal of current leaf remaining connection is 1 then neighbour is on edge
            if len(adj[neighbour]) == 1:
                next_leaves.append(neighbour)
        leaves = next_leaves
    return leaves


# Driver code
def main():
    input1 = [1, 2, 3, 4, 6]
    input2 = [[], [[0, 1]], [[0, 1], [1, 2]], [[1, 0], [1, 2], [2, 3]], [[0, 1], [0, 2], [0, 3], [0, 4], [4, 5]]]

    for i in range(len(input1)):
        print(str(i + 1) + ".\t", "n:", input1[i],
              "\n\t edges:", input2[i],
              "\n\n\t Root nodes that minimize the height:", min_height_trees(input1[i], input2[i]))

        print("-" * 100)

if __name__ == '__main__':
    main()