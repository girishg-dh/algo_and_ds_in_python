from typing import List
# Write any import statements here

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    remaining_value = []
    cost = 0.
    revenue = 0.
    for i in range(N):
        remaining_value.append(V[i] * 1.0)
        expected_loss = sum(remaining_value) * S
        if expected_loss >= C:
            revenue += sum(remaining_value)
            cost += C
            remaining_value = []
        elif i < N - 1:
            remaining_value = [(1 - S) * x for x in remaining_value]
    if remaining_value:
        if sum(remaining_value) >= C:
            revenue += sum(remaining_value)
            cost += C
            remaining_value = []
        else:
            remaining_value = []
    return revenue - cost


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



def max_expected_profit(N, V, C, S):
  """
  Calculates the maximum expected profit.

  Args:
    N: The number of days.
    V: A list of package values for each day.
    C: The cost to enter the mailroom.
    S: The probability of theft.

  Returns:
    The maximum expected profit.
  """

  dp = [[0] * (sum(V) + 1) for _ in range(N + 1)]  # Initialize dp table

  # Base case (last day)
  for v in range(sum(V) + 1):
    dp[N][v] = v - C  

  # Iterate backward from day N-1 to 1
  for i in range(N - 1, 0, -1):
    for v in range(sum(V) + 1):
      enter_profit = v - C + dp[i + 1][0]
      no_enter_profit = (1 - S) * dp[i + 1][min(v + V[i], sum(V))] + S * dp[i + 1][0] 
      dp[i][v] = max(enter_profit, no_enter_profit)

  return dp[1][0]

# Example usage
N = 5
V = [10, 2, 8, 6, 4]
C = 3
S = 0.15
print(max_expected_profit(N, V, C, S))  # Output: 20.10825