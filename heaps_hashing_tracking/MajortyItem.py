'''
Given an array, nums, having n integers, return the majority element. An element will be considered a majority element if it occurs more than
n / 2 times in the array.
'''

from collections import Counter
def find_majority_element(nums):
    c = Counter(nums)
    k, v = c.most_common(1)[0]
    if v * 2 > len(nums):
        return k
    else:
        return -1

print('most common element is : {}'.format(find_majority_element([7,7,5,5,7,5,7,5,7,5,7,5,7,7,5,5,7,5,5])))