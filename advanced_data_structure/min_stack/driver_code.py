from advanced_data_structure.min_stack.min_stack import MinStack
# driver code
def main():
    input_stacks = [
                   [[9, 3, 1, 4, 2, 5], [1, 1, 0, 1, 0, 1]],
                   [[5, 10, 6, 23, 2], [1, 1, 0, 1, 0]],
                   [[1, 2, 3, 4, 5, 6, -3, -8], [1, 1, 0, 1, 0, 1, 1, 0]],
                   [[14, 32, 66, 71, 22, 50, 35], [1, 0, 1, 1, 0, 1, 0]],
                   [[-2, 4, 5, 0, 1, -3], [1, 1, 1, 1, 1, 1]]
    ]

    # loop over all the input streams
    for i in range(len(input_stacks)):
        print(i + 1, ".\t Starting operations:", sep="")
        min_stack_obj = MinStack()

        for j in range(len(input_stacks[i][1])):
            if input_stacks[i][1][j] == 1:
                if input_stacks[i][0] == []:
                    next
                else:
                    print("\t\t Push(", input_stacks[i][0][j], ")", sep="")
                    min_stack_obj.push(input_stacks[i][0][j])
            else:
                print("\t\t Pop() returns ", min_stack_obj.pop(), sep="")
        print("\t Minimum number in the stack is: ",
              min_stack_obj.min_number(), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()
