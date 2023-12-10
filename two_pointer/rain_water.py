def rain_water_alternate(heights):
    current = 1
    water_store = 0
    while current < len(heights) - 1:
        left, right = current - 1, current + 1
        max_right, max_left = 0, 0
        while left >= 0 and right < len(heights):
            max_left = max(max_left, heights[left])
            max_right = max(max_right, heights[right])
            if(max_left< max_right):
                left -= 1
            else:
                right += 1
        minimax = min(max_left, max_right)
        if minimax > heights[current]:
             water_store = water_store + (minimax - heights[current])
        current += 1
    return water_store

def rain_water(heights):
    water_store = 0
    left, right = 0 , len(heights)-1
    right_max, left_max = 0, 0
    while left <= right:
        if left_max > right_max:
            water_store += max(0, right_max - heights[right])
            right_max = max(right_max, heights[right])
            right -= 1
        else:
            water_store += max(0, left_max - heights[left])
            left_max = max(left_max, heights[left])
            left += 1
    return water_store

if __name__ == "__main__":
    print(rain_water([1,0,3,0,1,2]))
    print(rain_water([0, 1, 3, 1, 0, 1, 4, 0, 2]))
    print(rain_water([0, 3, 0, 2, 1, 0, 1, 4, 2, 1, 2, 0]))