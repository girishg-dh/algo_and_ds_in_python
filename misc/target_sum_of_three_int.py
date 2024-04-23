def find_sum_of_three(nums, target):
    nums = sorted(nums)
    current = 0
    while current < len(nums) - 1:
        low, high = current+1, len(nums) - 1
        while low < high:
            current_sum = nums[low] + nums[current] + nums[high]
            if current_sum == target:
                return True
            elif current_sum < target:
                low += 1
            else:
                high -= 1
        current += 1
    return False


if __name__ == '__main__':
    print(find_sum_of_three([1, 2, 4, 6, 8, 20], 31))
    print(find_sum_of_three([1,-1,2], 2))
    print(find_sum_of_three([3,7,1,2,8,4,5], 10))
    print(find_sum_of_three([-1,2,1,-4,5,-3], -8))