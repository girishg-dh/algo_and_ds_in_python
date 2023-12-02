def product_except_self(arr: list):
    result = [1 for i in range(len(arr))]
    left_product, right_product = 1, 1 
    for i in range(len(arr)):
        left, right = i, len(arr) - i - 1
        result[left] *= left_product
        result[right] *= right_product
        left_product *= arr[left]
        right_product *= arr[right]
    return result


if __name__ == '__main__':
    print(product_except_self([0,-1,2,-3,4,-2]))
    print(product_except_self([2, 4, 3, -1, -2]))
    print(product_except_self([-1,2,3,5,0]))
