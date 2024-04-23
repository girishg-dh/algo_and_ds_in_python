def circular_array_loop(nums):
    index, slow, fast = 0, 0, 0
    for index in range(len(nums)):
        slow = fast = index
        current_direction = nums[index] > 0
        while True:
            slow = get_next_step(slow, nums)
            if is_not_possible(nums, current_direction, slow):
                break
            fast = get_next_step(fast, nums)
            if is_not_possible(nums, current_direction, fast):
                break
            fast = get_next_step(fast, nums)
            if is_not_possible(nums, current_direction, fast):
                break
            if slow == fast:
                return True

    return False

def get_next_step(current_index, nums):
    next_index = (current_index + nums[current_index]) % len(nums)
    if next_index < 0:
        next_index += len(nums)
    return next_index
    
    return next_index
def is_not_possible(nums, prev_direction, current_index):
    current_direction = nums[current_index] >= 0
    if(prev_direction != current_direction or abs(nums[current_index]) % len(nums) == 0):
        return True
    else:
        return False


def main():

    input = (
            [-2, -3, -9],
            [-5, -4, -3, -2, -1],
            [-1, -2, -3, -4, -5],
            [2, 1, -1, -2],
            [-1, -2, -3, -4, -5, 6],
            [1, 2, -3, 3, 4, 7, 1],
            [2, 2, 2, 7, 2, -1, 2, -1, -1]
            )
    num = 1

    for i in input:
        print(f"{num}.\tCircular array = {i}")
        print(f"\n\tFound loop = {circular_array_loop(i)}")
        print("-"*100, "\n")
        num += 1


if __name__ == "__main__":
    main()