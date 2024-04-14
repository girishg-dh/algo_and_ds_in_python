def combination_sum(nums, target)->list:
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    

# Driver code
def main():
    nums = [
            [2, 3, 5], 
            [3, 6, 7, 8], 
            [4, 5, 6, 9], 
            [20, 25, 30, 35, 40], 
            [3, 5, 7]
        ]

    targets = [5, 15, 11, 40, 15]

    for i in range(len(nums)):
            print(i+1, ".", "\tnums: ", nums[i], sep="")
            print("\tTarget: ", targets[i], sep="")
            combinations = combination_sum(nums[i], targets[i])
            print("\tNumber of Combinations: ", combinations, sep="")
            print("-" * 100)
            print()

if __name__ == '__main__':
    main()