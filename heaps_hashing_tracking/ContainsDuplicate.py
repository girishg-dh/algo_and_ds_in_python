from collections import Counter
def contains_duplicate(nums):
    collection = Counter(nums)
    return max(collection.values()) > 1

