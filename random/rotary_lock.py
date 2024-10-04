from typing import List 

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # Write your code here
    time = 0
    current_pos = 1
    for i in range(M):
        if C[i] == current_pos:
            continue
        elif C[i] > current_pos:
            time += min(C[i] - current_pos, N - C[i] + current_pos)
        else:
            time += min(current_pos - C[i], N - current_pos + C[i])
        current_pos = C[i]
    return time


print(getMinCodeEntryTime(10, 4, [9, 4, 4, 8]))
print(getMinCodeEntryTime(3, 3, [1,2,3]))
        