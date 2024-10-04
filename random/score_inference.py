from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
    solution_dict = dict()
    solution_dict[1] = 0 
    solution_dict[2] = 0
    for score in S:
        max_2s = score // 2
        max_1s = score % 2
        if solution_dict[2] < max_2s:
            solution_dict[2] = max_2s
        if solution_dict[1] < max_1s:
            solution_dict[1] = max_1s 
    return solution_dict[1] + solution_dict[2]


print(getMinProblemCount(6, [1, 2, 3, 4, 5, 6]))
print(getMinProblemCount(4, [4, 3, 3, 4]))
print(getMinProblemCount(4, [2, 4, 6, 8]))
