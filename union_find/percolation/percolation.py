from union_find.percolation.unionFind import UnionFind

import random
class Percolation:
    def __init__(self, n):
        self.n = n
        self.grid = [[0] * n for _ in range(n)]
        self.uf = UnionFind(n * n + 2)
        self.virtual_top = n * n
        self.virtual_bottom = n * n + 1
        self.open_sites = 0
    
    def is_valid(self, row, col):
        return 0 <= row < self.n and 0 <= col < self.n
    def index(self, row, col):
        return row * self.n + col
    
    def percolates(self):
        return self.uf.find(self.virtual_top) == self.uf.find(self.virtual_bottom)
    def reset(self):
        self.grid = [[0] * self.n for _ in range(self.n)]
        self.uf = UnionFind(self.n * self.n + 2)
        self.open_sites = 0


    def open_site(self, row, col):
        if not self.grid[row][col]:
            self.grid[row][col] = 1
            self.open_sites += 1
            
            if row == 0:
                self.uf.union(self.index(row, col), self.virtual_top)
            elif row == self.n - 1:
                self.uf.union(self.index(row, col), self.virtual_bottom)
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + dr, col + dc
                if self.is_valid(new_row, new_col) and self.grid[new_row][new_col]:
                    self.uf.union(self.index(row, col), self.index(new_row, new_col))
    def percolation_threshold(self, trials):
        for _ in range(trials):
            self.reset()
            while not self.percolates():
                row = random.randint(0, self.n - 1)
                col = random.randint(0, self.n - 1)
                self.open_site(row, col)
            return self.open_sites / (self.n * self.n)