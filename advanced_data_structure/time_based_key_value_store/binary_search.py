# Implementation of binary search for searching in a time based key value store data structure
def binary_search(array, key):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    # If the key is not found, return the index of the largest element smaller than the key
    return high
