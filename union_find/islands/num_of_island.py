from union_find.islands.union_find import UnionFind

def is_valid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def num_islands(grid):
    uf = UnionFind(grid)
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                grid[i][j] = '0'
                for x, y in delta:
                    if is_valid(grid, i + x, j + y) and grid[i + x][j + y] == '1':
                        uf.union(i * len(grid[0]) + j, (i + x) * len(grid[0]) + (j + y))
    return uf.count


# Driver code
def main():
    
    # Example grids
    # Test case 01
    grid1 = [
        ['1', '1', '1'],
        ['0', '1', '0'],
        ['1', '0', '0'],
        ['1', '0', '1']
    ]

    # Test case 02
    grid2 = [
        ['1', '1', '1', '1', '0'],
        ['1', '0', '0', '0', '1'],
        ['1', '0', '0', '1', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '1', '0', '1', '1']
    ]

    # Test case 03
    grid3 = [
        ['1', '1', '1', '1', '0'],
        ['1', '0', '0', '0', '1'],
        ['1', '1', '1', '1', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '1', '0', '1', '1']
    ]

    # Test case 04
    grid4 = [
        ['1', '0', '1', '0', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '0', '1', '0', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '0', '1', '0', '1']
    ]

    # Test case 05
    grid5 = [
        ['1', '0', '1'],
        ['0', '0', '0'],
        ['1', '0', '1']
    ]

    inputs = [grid1, grid2, grid3, grid4, grid5]
    num = 1

    for i in inputs:
        print(num, ".\tGrid:", sep = "")
        print_grid(i)
        print('\n\t Output :', num_islands(i))
        print('-' * 100)
        num += 1

def print_grid(grid):
    for i in grid:
        print(i)

if __name__ == "__main__":
    main()