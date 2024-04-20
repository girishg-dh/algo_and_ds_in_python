'''Imagine a scenario where an adventurous little robot, named Robi, has a mission to traverse 
a grid with m rows and n columns and reach a treasure box placed grid[m,n] . Robi starts the journey 
from its home in the top-left corner of the grid,  grid[0,0]. However, it faces a constraint that at 
any given time, it can only move in either of the two directions: downward or to the right. Given the
 two integers, m and n, return the total number of unique paths that Robi can take from the grid's top-left 
 corner to reach the bottom-right corner of the grid.'''

import math

def unique_paths_math(m, n):
	return math.factorial(m + n - 2) // (math.factorial(m - 1) * math.factorial(n - 1))

def unique_paths(m, n):
	dp = [[1] * n for _ in range(m)]
	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = dp[i-1][j] + dp[i][j-1]
	return dp[m-1][n-1]

# Driver code
def main():
	input = (
		[1, 1],
        [2, 3],
        [4, 4],
        [2, 5],
		[10, 10],
		[1, 30]
    )
	print("S: Source, D: Destination")
	print("-"*100)
	for i in range(len(input)):
		print(i + 1, ".\tm = ", input[i][0], ", n = ", input[i][1], sep="")
		print("\n\tThe grid: ")
		print_grid(input[i][0], input[i][1])
		ans = unique_paths(input[i][0], input[i][1])
		print("\n\tTotal unique paths: ", ans)
		print("-"*100)



def print_grid(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                  print("S", end=" ")
            elif i == m -1 and j == n-1:
                print("D", end=" ")
            else:
                print(".", end=" ")
        print()

if __name__ == '__main__':
    main()