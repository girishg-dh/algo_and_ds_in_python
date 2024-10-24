from typing import List
# Write any import statements here

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    # Create a list of strategies for each day where each entry is 
    # (remaining_value, collected_profit)
    best_strategy = [(0,0)]
    for mail_price in V:
        #Add strategy for the new day
        best_strategy.insert(0, (0, 0))

        # For all remainig value must be reduced by prob of stealing
        best_strategy = [(remaining_value * (1 - S), collected_profit) for remaining_value, collected_profit in best_strategy]

        # Option 1: Pick up today
        # Find the best strategy so far and add current profit
        best_of_all = max(collected_profit + remaining_value for remaining_value, collected_profit in best_strategy) + mail_price - C
        best_strategy[0] = (0, best_of_all)

        # Option 2: Don't pick up today
        # Add mail_price to remaining value
        for i in range(1, len(best_strategy)):
            remaining_value, collected_profit = best_strategy[i]
            best_strategy[i] = (remaining_value + mail_price, collected_profit)
        # Repeat for next day 
    return max(collected_profit for remaining_value, collected_profit in best_strategy)
        


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

