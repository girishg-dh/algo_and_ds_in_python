def binary_search_rotated(nums, target):
  # Replace this placeholder return statement with your code
    l = len(nums)
    first, last = 0, l-1
    if l == 1 :
        if target == nums[0]:
            return 0 
        else:
            return -1
    while first <= last:
        mid = (first + last) // 2
        if target == nums[mid]:
            return mid
        if nums[mid] < nums[last]:
            if nums[mid] <= target and nums[last] >= target:
                first = mid+1
            else: last = mid 
        elif nums[first] < nums[mid]:
            if nums[first] <= target and target <= nums[mid]:
                last = mid
            else: first = mid +1
    return -1



if __name__=="__main__":
    n1, t1 = [6,7,1,2,3,4,5], 3
    n2, t2 = [4,5,6,1,2,3], 6
    n3, t3 = [4], 1
    print(binary_search_rotated(n1, 6))
    print(binary_search_rotated(n1, t1))
    print(binary_search_rotated(n2, t2))
    print(binary_search_rotated(n2, 6))
    print(binary_search_rotated(n2, 3))
    print(binary_search_rotated(n3, t3))
