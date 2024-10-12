import math 


def findSignatureCounts(arr):
    # Write your code here
    result = [0] * len(arr)
    for i in range(len(arr)):
        result[i] = i + 1
    for i in range(len(arr)):
        result[arr[i] - 1] = i + 1
    return result



arr_1 = [2, 1]
expected_1 = [2, 2]
output_1 = findSignatureCounts(arr_1)
print(output_1)