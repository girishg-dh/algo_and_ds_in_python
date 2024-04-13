class Neighbours:
    def __init__(self) -> None:
        self.grid = [[]]

    def left(grid, x, y):
        if y > 0:
            return grid[x][y-1]
        else:
            return None
    
    def right(grid, x, y):
        if y < len(grid[x])-1:
            return grid[x][y+1]
        else:
            return None 
    
    def up(self, grid, x, y):
        if x > 0:
            return grid[x-1][y]
        else:
            return None
    
    def down(self, grid, x, y):
        if x < len(grid)-1:
            return grid[x+1][y]
        else:
            return None

    def all(self, grid, x, y):
        return [self.left(grid, x, y), self.right(grid, x, y), self.up(grid, x, y), self.down(grid, x, y)]