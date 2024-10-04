"""In a pond, a frog family embarks on a journey toward dry land for hibernation. They plan to traverse a trail of N lily pads, numbered from 1 to N in order. 
There are F frogs, also numbered from 1 to F. Each frog i is initially perched on lily pad Pi. No two frogs start on the same lily pad. 
Lily pad N is adjacent to the shore, and initially, none of the frogs are on it.
Each second, a single frog may hop along the trail toward lily pad N. When a frog hops, it moves to the nearest lily pad after its current
 lily pad which is not occupied by another frog (leaping over any frogs on intermediate lily pads). 
If this causes it to reach lily pad N, it immediately exits onto the shore. Multiple frogs cannot hop simultaneously during the same second.
Assuming the frogs collaborate optimally when deciding which frog should hop each second, we need to determine the minimum number of seconds 
required for all F frogs to reach the shore.
"""

"""
Sort the initial positions of the frogs in descending order.
For each frog, calculate the number of seconds it needs to reach the shore:
The rightmost frog needs (N - its_position) seconds.
Each subsequent frog needs max(previous_frog_time + 1, N - its_position) seconds.

The time for the last frog to reach the shore is the total time needed."""

from typing import List

def getSecondsRequired(N, F, P):
    positions = sorted(P, reverse = True)
    total_time = 0 
    for i, pos in enumerate(positions):
        frog_time = N - pos
        if i == 0:
            total_time = frog_time
        else: 
            total_time = max(total_time + 1, frog_time)
    return total_time
        
    


    


print(getSecondsRequired(3, 1, [1])) # Expected output = 1
print(getSecondsRequired(6, 3, [5, 2, 4])) # Expected output = 4
print(getSecondsRequired(5, 2, [1, 3])) # Expected output = 2
print(getSecondsRequired(4, 4, [1, 2, 3, 4])) # Expected output = 3
print(getSecondsRequired(10, 5, [1, 2, 3, 4, 5])) # Expected output = 4


