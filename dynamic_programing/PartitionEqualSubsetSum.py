
def can_partition_array(arr):
    n = len(arr)
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False 
    target = total_sum // 2
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for j in range(target, arr[i-1] - 1, -1):
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
    return dp[n][target]
# Driver code
def main():
    arr = [[3, 1, 1, 2, 2, 1], [1, 3, 7, 3], [1, 2, 3], [1, 2, 5],
    [1, 3, 4, 8], [1, 2, 3, 2, 3, 5], [1, 5, 3, 2, 3, 19, 3],
    [1, 2, 3, 5, 3, 2, 1]]
    
    for i in range(len(arr)):
        print(i + 1,  ". Input array: ", arr[i], sep="")
        result = can_partition_array(arr[i])
        print("\nCan we partition the array into equal sum arrays?: ",
              bool(result), sep="")
        print("-" * 100)

if __name__ == "__main__":
    main() 