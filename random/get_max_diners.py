from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  S.sort()
  S.append(N+K+1)
  S.insert(0, -K)
  print(S)
  count = 0
  for i in range(1, M+2):
    if S[i] - S[i-1] > K:
      count += (S[i] - S[i-1] - K - 1) // (K+1)
  return count


# NOTE: The following input values will be used for testing your solution.




print("Max new diners:" ,getMaxAdditionalDinersCount(10, 1, 2, [2, 6]))
print("Max new diners:", getMaxAdditionalDinersCount(15, 2, 3, [11, 6, 14]))
print("Max new diners:", getMaxAdditionalDinersCount(10, 1, 0, []))
