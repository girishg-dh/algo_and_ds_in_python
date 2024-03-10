'''
Consider an m x n grid containing cells with three potential values:
0: which indicates an unoccupied cell.
1: representing a freshly picked orange.
2: indicating a rotten orange.
Any fresh orange that is 4–directionally adjacent to a rotten orange will also turn rotten with each passing minute.

Your task is to determine the minimum time required for all cells to have rotten oranges. In case, this objective cannot be achieved,
return -1
'''


from collections import deque

def min_minutes_to_rot(grid):
    r,c = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    current = deque()
    hasone = 0
    minutes = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 2:
                current.append((i,j))
            if grid[i][j] == 1:
                hasone += 1

    while len(current)>0:
        for _ in range(len(current)):
            c_i, c_j = current.popleft()
            for dx, dy in directions:
                next_row , next_col = c_i + dx , c_j + dy
                if 0 <= next_row < r and 0 <= next_col < c and grid[next_row][next_col] == 1:
                    grid[next_row][next_col] = 2
                    current.append((next_row, next_col))
                    hasone -= 1
        minutes += 1
    return -1 if hasone > 0 else max(0, minutes-1)

def main():
    inputs = [
                [[2, 1, 0],
                 [1, 1, 1],
                 [1, 0, 0]],

                [[2, 0, 2, 0],
                 [2, 0, 2, 0],
                 [2, 0, 2, 0],
                 [2, 0, 2, 0]],

                [[1, 1, 1, 1, 1],
                 [1, 0, 0, 1, 0],
                 [0, 1, 2, 1, 1],
                 [0, 0, 1, 1, 0],
                 [1, 1, 1, 0, 0]],

                [[2, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1],
                 [1, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1]],

                [[2, 0, 1],
                 [1, 0, 2],
                 [0, 1, 1]]
    ]
    for i in inputs:
        print(min_minutes_to_rot(i))

if __name__=="__main__":
    main()