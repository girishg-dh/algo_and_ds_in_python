from typing import List
# Write any import statements here

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
  # Write your code here
  dp = [[0] * (sum(V)+1) for _ in range(N+1)]
  for v in range(sum(V)+1):
    dp[N][v] = v - C
    
  for i in range(N-1, 0, -1):
    for v in range(sum(V) + 1):
      enter_profit = v - C + dp[i+1][0]
      no_enter_profit = (1 - S) * dp[i+1][min(sum(V), v + V[i])] + S * dp[i+1][0]
      dp[i][v] = max(enter_profit, no_enter_profit)
  return dp[1][0]


N = 5
V = [10, 2, 8, 6, 4]
C = 5
S = 0.0
print(getMaxExpectedProfit(N, V, C, S))

N = 5
V = [10, 2, 8, 6, 4]
C = 5
S = 1.0
print(getMaxExpectedProfit(N, V, C, S))

N = 5
V = [10, 2, 8, 6, 4]
C = 3
S = 0.5
print(getMaxExpectedProfit(N, V, C, S))

N = 5
V = [10, 2, 8, 6, 4]
C = 3
S = 0.15
print(getMaxExpectedProfit(N, V, C, S))

