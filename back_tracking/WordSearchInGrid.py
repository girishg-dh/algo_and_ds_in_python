
from neighbours import neighbours
from backtracking import backtracking

def word_search(grid, word):
    




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