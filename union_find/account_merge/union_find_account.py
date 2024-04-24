class unionFind:
    def __init__(self, n):
        """
        Initializes the unionFind object with a list of parents containing values from 0 to n-1.
        
        Parameters:
            n (int): The number of elements to initialize the parent list with.
        
        Returns:
            None
        """
        self.parent = list(range(n))

    def find(self, x):
        """
        Recursively find the root parent of the input element x in the unionFind object.
        
        Parameters:
            x (int): The element to find the root parent for.
        
        Returns:
            int: The root parent of the input element x.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """
        Merge two sets containing elements x and y.

        Parameters:
            x (int): The first element.
            y (int): The second element.

        Returns:
            None: This function does not return anything.

        This function finds the root parents of elements x and y using the find() method. If the root parents are different, it sets the parent of the root parent of x to the root parent of y. This effectively merges the sets containing x and y.

        Example:
            >>> uf = unionFind(5)
            >>> uf.union(0, 2)
            >>> uf.parent
            [0, 0, 0, 3, 4]
        """
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.parent[rootx] = rooty