def grid_to_uppper(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = grid[i][j].upper()
    return grid

def dfs(grid, word, row, col, index, visited):
    if index == len(word): 
        return True 
    if(0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == word[index] and not visited[row][col]):
        visited[row][col] = True 
        if (dfs(grid, word, row, col + 1, index + 1, visited) or 
            dfs(grid, word, row + 1, col, index + 1, visited) or 
            dfs(grid, word, row - 1, col, index + 1, visited) or 
            dfs(grid, word, row, col - 1, index + 1, visited)):
            return True
        visited[row][col] = False
    return False


def word_search(grid, word):
   if not grid or not word:
       return False
   
   word = word.upper()
   grid = grid_to_uppper(grid)
   visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
   for i in range(len(grid)):
        for j in range(len(grid[i])):
            if dfs(grid, word, i, j, 0, visited):
                return True
   return False
    




#Driver code
def main():
    input = [
             ([['E', 'D', 'X', 'I', 'W'],
              ['P', 'U', 'F', 'M', 'Q'],
              ['I', 'C', 'Q', 'R', 'F'],
              ['M', 'A', 'L', 'C', 'A'],
              ['J', 'T', 'I', 'V', 'E']], "educative"),
              
             ([['E', 'D', 'X', 'I', 'W'],
              ['P', 'A', 'F', 'M', 'Q'],
              ['I', 'C', 'A', 'S', 'F'],
              ['M', 'A', 'L', 'C', 'A'],
              ['J', 'T', 'I', 'V', 'E']], "PACANS"),

              ([['h', 'e', 'c', 'm', 'l'],
              ['w', 'l', 'i', 'e', 'u'],
              ['a', 'r', 'r', 's', 'n'],
              ['s', 'i', 'i', 'o', 'r']], "WARRIOR"),

              ([['C', 'Q', 'N', 'A'],
              ['P', 'S', 'E', 'I'],
              ['Z', 'A', 'P', 'E'],
              ['J', 'V', 'T', 'K']], "save"),

             ([['O', 'Y', 'O', 'I'],
              ['B', 'I', 'E', 'M'],
              ['K', 'D', 'Y', 'R'],
              ['M', 'T', 'W', 'I'],
              ['Z', 'I', 'T', 'O']], "DYNAMIC"),
            ]
    num = 1

    for i in input:
        print(num, ".\tGrid =", sep="")
        for j in range(len(i[0])):
            print("\t\t", i[0][j])
        if i[1] == "":
            print('\n\tWord = ""')
        else:
            print(f"\n\tWord =  {i[1]}")
        print("\n\tProcessing...")
        search_result = word_search(i[0], i[1])
        if search_result:
            print("\n\tSearch result = Found Word")
        else:
            print("\n\tSearch result = Word could not be found")
        num += 1
        print("-"*100, "\n")


if __name__ == "__main__":
    main()