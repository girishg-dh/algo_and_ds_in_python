def container_with_most_water(height:list)->int:
    # Replace this placeholder return statement with your code
    max_water = 0
    l, r = 0, len(height)-1
    while l<r:
        max_water = max(max_water, (r-l)* min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_water


if __name__ == '__main__':
    print(container_with_most_water([1,8,6,2,5,4,8,3,7]))
    print(container_with_most_water([1,1]))
    print(container_with_most_water([2,8,6,3,5,4,7]))
    print(container_with_most_water([1,5]))
    print(container_with_most_water([7,7,2]))