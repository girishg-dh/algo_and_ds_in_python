"""
Problem: Find the longest consecutive sequence of integers in an unsorted array
Approach: Use union find to find the longest consecutive sequence
Complexity: O(n)
To find the longest consecutive sequence of integers in an unsorted array, you can use a simple algorithm. Here's the approach:
First, create a set from the elements of the array for efficient lookup.
Then, iterate through each element of the array.
For each element, check if it's the start of a sequence by looking for its consecutive elements in the set. If an element has no preceding element in the set, it marks the start of a sequence.
For each start element found, continue counting consecutive elements until no more consecutive elements are found in the set.
Update the longest consecutive sequence found during this process.
"""

def longest_consecutive_seq(arr):
    if not arr:
        return 0
    arr_set = set(arr)
    max_len = 0
    for elem in arr_set:
        if elem - 1 not in arr_set:
            current_num = elem
            current_len = 1
            while current_num + 1 in arr_set:
                current_num += 1
                current_len += 1
            max_len = max(current_len, max_len)
    return max_len
    



def main():
    arr = [100, 4, 200, 1, 3, 2]
    print(longest_consecutive_seq(arr))
    arr = [78, 2, 32, 4, 1, 3]
    print(longest_consecutive_seq(arr))

if __name__ == '__main__':
    main()