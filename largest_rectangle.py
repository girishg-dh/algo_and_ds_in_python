def largest_rectangle(heights: list) -> int:
    stack = []
    max_area = 0
    stack.append(-1)
    current_index = 0
    while current_index < len(heights):
        if stack[-1] == -1 :
            stack.append(current_index)
            current_index += 1
        elif heights[stack[-1]] <= heights[current_index]:
            stack.append(current_index)
            current_index += 1
        else:
            last_index = stack.pop()
            width = current_index - stack[-1] - 1
            area = width * heights[last_index]
            max_area = max(max_area, area)
    while stack[-1] != -1 and len(stack)>0:
        last_index = stack.pop()
        width = current_index - stack[-1] -1
        area = width * heights[last_index]
        max_area = max(area, max_area)
    return max_area




if __name__ == '__main__':
    # print(largest_rectangle([2,4,5,7,3,9]))
    heights = [
        [1, 3, 4, 2, 2],
        [2, 1, 5, 6, 2, 3],
        [2, 4, 5, 7, 3, 9],
        [1, 2, 3, 4, 5],
        [3, 1, 3, 4, 2, 1, 5, 4, 2, 3, 1, 2, 3, 2, 4, 1, 2, 2, 5, 3],
        [1, 2, 3, 2, 5, 6, 2, 1, 4, 3, 2, 3, 4, 1, 3, 2, 3, 4, 5, 1]
    ]
    for h in heights:
        print(largest_rectangle(h))