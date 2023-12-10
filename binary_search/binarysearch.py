def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r-l) // 2
        if target == nums[m]:
            return m
        elif target > nums[m]:
            l = m + 1
        else:
            r = m - 1 

    # Replace this placeholder return statement with your code
    return -1
