def max_sub_array(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(current_sum, max_sum)
    return max_sum

# Driver code
def main():
    inputs = [[1, 2, 2, 3, 3, 1, 4], 
              [2, 2, 1], 
              [4, 1, 2, 1, 2], 
              [-4, -1, -2, -1, -2], 
              [25]]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\tResult: ", max_sub_array(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()