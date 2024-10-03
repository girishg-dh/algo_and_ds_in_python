"""
A photography set consists of N cells in a row, numbered from 1 to N in order, and can be represented by a string C of length N. 
Each cell i is one of the following types 
(indicated by Cij, the ith character of C): 
If Ci “P”, it is allowed to contain a photographer 
If Ci= “A”, it is allowed to contain an actor 
If Ci = “B”, it is allowed to contain a backdrop 
If Ci = “.”, it must be left empty A photograph consists of a photographer, an actor, and a backdrop, 
such that each of them is placed in a valid cell, and such that the actor is between the photographer and the backdrop. 
Such a photograph is considered artistic if the distance between the photographer and the actor is between X and Y cells (inclusive), 
and the distance between the actor and the backdrop is also between X and Y cells (inclusive). 
The distance between cells i and j is |i - j|(the absolute value of the difference between their indices). 
Determine the number of different artistic photographs which could potentially be taken at the set. 
Two photographs are considered different if they involve a different photographer cell, actor cell, and/or backdrop cell.
"""


def count_artistic_photo(N: int, X: int, Y : int, C : str):
    # Helper function to count valid combinations
    def count_combinations(start, end, target):
        return sum(1 for i in range(start, end) if C[i] == target)

    total = 0
    
    # Iterate through all possible actor positions
    for actor in range(N):
        if C[actor] != 'A':
            continue
        
        # Count photographers to the left
        left_p = count_combinations(max(0, actor - Y), max(0, actor - X + 1), 'P')
        
        # Count backdrops to the right
        right_b = count_combinations(min(N, actor + X), min(N, actor + Y + 1), 'B')
        
        # Count photographers to the right
        right_p = count_combinations(min(N, actor + X), min(N, actor + Y + 1), 'P')
        
        # Count backdrops to the left
        left_b = count_combinations(max(0, actor - Y), max(0, actor - X + 1), 'B')
        
        # Add combinations: (left photographers * right backdrops) + (right photographers * left backdrops)
        total += left_p * right_b + right_p * left_b

    return total


print("v1", count_artistic_photo(5, 1, 2, "APABA"))  # Output: 1
print("v1", count_artistic_photo(5, 2, 3, "APABA"))  # Output: 3
print("v1", count_artistic_photo(8, 1, 1, "PPPABAPB"))  # Output: 5
print("v1", count_artistic_photo(8, 1, 3, ".PBAAP.B"))  # Output: 3


## Optimized 
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Precompute cumulative counts of P and B
    p_cumulative = [0] * (N + 1)
    b_cumulative = [0] * (N + 1)
    
    for i in range(N):
        p_cumulative[i + 1] = p_cumulative[i] + (C[i] == 'P')
        b_cumulative[i + 1] = b_cumulative[i] + (C[i] == 'B')
    
    total = 0
    
    # Iterate through all possible actor positions
    for actor in range(N):
        if C[actor] != 'A':
            continue
        
        # Count photographers to the left
        left_p = p_cumulative[max(0, actor - X + 1)] - p_cumulative[max(0, actor - Y)]
        
        # Count backdrops to the right
        right_b = b_cumulative[min(N, actor + Y + 1)] - b_cumulative[min(N, actor + X)]
        
        # Count photographers to the right
        right_p = p_cumulative[min(N, actor + Y + 1)] - p_cumulative[min(N, actor + X)]
        
        # Count backdrops to the left
        left_b = b_cumulative[max(0, actor - X + 1)] - b_cumulative[max(0, actor - Y)]
        
        # Add combinations: (left photographers * right backdrops) + (right photographers * left backdrops)
        total += left_p * right_b + right_p * left_b

    return total

# Test cases
print("v2", getArtisticPhotographCount(5, "APABA", 1, 2))  # Output: 1
print("v2", getArtisticPhotographCount(5, "APABA", 2, 3))  # Output: 3
print("v2", getArtisticPhotographCount(8, "PPPABAPB", 1, 1))  # Output: 5
print("v2", getArtisticPhotographCount(8, ".PBAAP.B", 1, 3))  # Output: 3

