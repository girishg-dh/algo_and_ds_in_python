from typing import List


def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    count = 0 
    if N == 1:
        return 0
    if N == 0:
        return -1
    for i in range(N-1, 0, -1):
        if R[i] <= R[i-1]:
            count += 1
            R[i-1] = R[i] - 1
            if R[i-1] <= 0:
                return -1
    return count


print(getMinimumDeflatedDiscCount(5, [2, 5, 3, 6, 5]))
print(getMinimumDeflatedDiscCount(3, [100, 100, 100]))
print(getMinimumDeflatedDiscCount(4, [6, 5, 4, 3]))