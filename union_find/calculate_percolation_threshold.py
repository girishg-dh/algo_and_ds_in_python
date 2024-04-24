from union_find.percolation import *

for n in range(1,6):
    print(f"Percolation threshold for {n}x{n} grid: {Percolation(n).percolation_threshold(1000)}")
