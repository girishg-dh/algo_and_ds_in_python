class neighbours:
    def __init__(self) -> None:
        self.grid = [[]]

    def left(grid, x, y):
        return grid[x][y-1]
    
    def right(grid, x, y):
        return grid[x][y+1]
    
    def up(grid, x, y):
        return grid[x-1][y]
    
    def down(grid, x, y):
        return grid[x+1][y]