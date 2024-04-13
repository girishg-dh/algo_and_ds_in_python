def flood_fill(grid, sr, sc, target):
    source_value = grid[sr][sc]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = [(sr, sc)]
    grid[sr][sc] = target
    while queue:
        row, col = queue.pop(0)
        for direction in directions:
            new_row, new_col = row + direction[0], col + direction[1]
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == source_value:
                grid[new_row][new_col] = target
                queue.append((new_row, new_col))
    return grid

def print_grid(grid, pre_msg):
    print(pre_msg, sep = "")
    for row in grid:
        print(row)

def main():
    grids = [[ 
                [1, 1, 0, 1, 0], 
                [0, 0, 0, 0, 1], 
                [0, 0, 0, 1, 1], 
                [1, 1, 1, 1, 0], 
                [1, 0, 0, 0, 0]
            ],
            [   
                [1, 1, 0, 1], 
                [0, 0, 0, 0], 
                [0, 0, 0, 1], 
                [1, 1, 1, 1]
            ],
            [   
                [9, 9, 6, 9], 
                [6, 9, 9, 6], 
                [6, 9, 9, 9], 
                [9, 9, 9, 9]
            ],
            [   
                [1, 1, 0, 1], 
                [0, 1, 0, 0], 
                [0, 1, 1, 0], 
                [1, 0, 1, 1]
            ],
            [   
                [1, 2, 0, 0], 
                [3, 1, 3, 6], 
                [7, 2, 1, 5], 
                [1, 9, 2, 1]
            ]]

    starting_row = [4, 2, 2, 2, 1]
    starting_col = [3, 3, 1, 3, 1]
    new_target = [3, 2, 1, 0, 4]

    for i in range(len(grids)):
        print_grid(grids[i], f'{i+1}Grid before flood fill: ')
        print("Starting row and column are: (" , starting_row[i], ", ", starting_col[i], ")", sep = "")
        print("Target value: ", new_target[i], sep = "")
        response = flood_fill(grids[i], starting_row[i], starting_col[i], new_target[i])
        print_grid(response, f'{i+1}Grid after flood fill: ')
        print("-" * 100)




if __name__ == '__main__':
    main()