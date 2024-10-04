"""
There are N dishes in a row on a kaiten belt, with the ith dish being of type Di. Some dishes may be of the same type as one another.
You're very hungry, but you'd also like to keep things interesting. 
The N dishes will arrive in front of you, one after another in order, and for each one you'll eat it as long as it isn't the same type as any of the previous 
K dishes you've eaten. You eat very fast, so you can consume a dish before the next one gets to you. Any dishes you choose not to eat as they pass will be eaten by others.
Determine how many dishes you'll end up eating.
Please take care to write a solution which runs within the time limit.
Constraints
1≤N≤500,000
1≤K≤N
1≤D i ≤1,000,000
"""


from typing import List
from random import randint
from collections import deque

def getMaximumEatenDishCount(N, D, K):
    eaten_dishes = set()  # To track the last K eaten dishes
    last_k_dishes = deque()  # To keep the order of the last K eaten dishes
    eaten_count = 0  # To count how many dishes you've eaten

    for dish in D:
        if dish not in eaten_dishes:
            # Eat the dish
            eaten_count += 1
            eaten_dishes.add(dish)
            last_k_dishes.append(dish)
            
            # If we've eaten more than K dishes, remove the oldest one
            if len(last_k_dishes) > K:
                oldest_dish = last_k_dishes.popleft()
                eaten_dishes.remove(oldest_dish)

    return eaten_count

print(getMaximumEatenDishCount(6, [1, 2, 3, 3, 2, 1], 1))
print(getMaximumEatenDishCount(6, [1, 2, 3, 3, 2, 1], 2))
print(getMaximumEatenDishCount(7, [1, 2, 1, 2, 1, 2, 1], 2))

print(getMaximumEatenDishCount(500, [randint(1, 100) for _ in range(500)], 10))



# print(timeit.timeit('getMaximumEatenDishCount(500, [randint(1, 100) for _ in range(500)], 10)', globals=globals()))

