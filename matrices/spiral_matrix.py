def spiral_order(matrix):
   rUp, cUp = len(matrix), len(matrix[0])
   result_length = rUp * cUp
   rLo, cLo = 0, 0
   direction = 1 # 1 = top to bottom and left to right, -1 = right to left and bottom to top
   i = j = 0
   result = []
   while True:
    if len(result) == result_length:
       return result

    if direction == 1:
        result.append(matrix[i][j])
        if j < cUp-1:
            j += 1
        elif i < rUp-1:
           i += 1
        else:
           direction *= -1
           rLo += 1
           cUp -= 1
    else:
        if j > cLo:
           j -= 1
           result.append(matrix[i][j])
        elif i > rLo:
            i -= 1
            result.append(matrix[i][j])
        else:
           direction *= -1
           cLo += 1
           rUp -= 1
           i, j = rLo, cLo
# Driver code
def main():
    inputs = [[[10, 1, 14, 11, 14], [13, 4, 8, 2, 13], [10, 19, 1, 6, 8], [20, 10, 8, 2, 12], [15, 6, 8, 8, 18]]]

    for i in range(len(inputs)):
        print(i + 1, ".\tMatrix:", sep="")
        print_matrix(inputs[i])

        print("\n\tSpiral order:", spiral_order(inputs[i]))
        print("-" * 100)

def print_matrix(matrix):
   for i in range(len(matrix)):
      for j in range(len(matrix[0])):
         print('{0:3d}'.format(matrix[i][j]), end="")
      print()

if __name__ == "__main__":
    main()