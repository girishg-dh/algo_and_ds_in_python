def find_all_subsets(nums):
    subsets = [[]]
    for num in nums:
        for i in range(len(subsets)):
            curr_subset = subsets[i]
            subsets.append(curr_subset + [num])
    return subsets


def main():
    nums = [[], [2, 5, 7], [1, 2], [1, 2, 3, 4], [7, 3, 1, 5]]

    for i in range(len(nums)):
        print(i + 1, ". Set:     ", nums[i], sep='')
        print(i + 1, ". Subsets: ", find_all_subsets(nums[i]), sep='')
        print(i + 1, ". Length:  ", len(find_all_subsets(nums[i])), sep='')
        print("-"*100)


if __name__ == '__main__':
    main()