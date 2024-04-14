import math

def update_matrix(mat):
    distance_matrix = [[math.inf for i in range(len(mat[0]))] for j in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                distance_matrix[i][j] = 0
            else:
                #check left
                if j > 0:
                    distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][j - 1] + 1)
                #check top
                if i > 0:
                    distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i - 1][j] + 1)
        #reverse traversal of mat
        for j in range(len(mat[0]) - 1, -1, -1):
            for i in range(len(mat) - 1, -1, -1):
                #check right
                if j < len(mat[0]) - 1:
                    distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][j + 1] + 1)
                #check bottom
                if i < len(mat) - 1:
                    distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i + 1][j] + 1)

    # Replace this placeholder return statement with your code
    return distance_matrix



def print_matrix(mat):
    for i in range(len(mat)):
        print("\t", mat[i])

# Driver code
def main():
    input_bits = [
        [[0, 1], [1, 1]],
        [[0, 0, 1], [0, 1, 1], [1, 0, 1]],
        [[0, 0, 0], [0, 1, 0], [1, 0, 1]],
        [[0, 0, 0], [0, 1, 0], [1, 1, 1]],
        [[0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]],
        [[0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 1]],
    ]

    for i in range(len(input_bits)):
        print(i + 1, ".\t Input matrix: ", sep="")
        print_matrix(input_bits[i])
        print("\n\t Distance matrix: ", sep="")
        print_matrix(update_matrix(input_bits[i]))
        print("-" * 100)

if __name__ == "__main__":
    main()