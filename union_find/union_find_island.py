class UnionFind:
    # Initializing the parent list and count variable by traversing the grid
    def __init__(self, grid):
        """
        Initializes the UnionFind object based on the grid provided.

        Parameters:
            grid (List[List[int]]): A 2D grid representing the components.

        Returns:
            None
        """
        self.parent = []
        self.rank = []
        self.count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent.append(i*n+j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)
    # Function to find the root parent of a node
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
     
     # Function to connect components
    def union(self, i, j):
        """
        Connects the components represented by nodes i and j in the union-find data structure.
        
        Parameters:
            self (UnionFind): An instance of the UnionFind class.
            i (int): The first node to be connected.
            j (int): The second node to be connected.
            
        Returns:
            None
        """
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            self.count -= 1
     # Function to return the number of conencted components consisting of "1"s
    def get_count(self):
       """
       Returns the count of connected components in the UnionFind object.

       :return: An integer representing the count of connected components.
       """
       return self.count

