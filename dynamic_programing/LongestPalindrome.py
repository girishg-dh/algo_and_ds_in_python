
def longest_palindromic_substring(string):
    """
    Function to find the length of the longest palindromic substring in a given string
    """
    # Create a 2D array to store the length of the longest palindromic substring
    # for each substring of the given string

    # Create a 2D array to store the length of the longest palindromic substring
    # for each substring of the given string
    length = len(string)
    dp = [[False] * length for i in range(length)]

    # Initialize the longest palindromic substring to be a single character

# Driver code
def main():
    """
    Driver function to test the longest palindromic substring function
    """
    strings = ['cat', 'lever', 'xyxxyz', 'wwwwwwwwww', 'tattarrattat']
    
    for i in range(len(strings)):
        # Print the input string
        print(i + 1, ".\t Input string: '", strings[i], "'", sep="")
        # Call the longest palindromic substring function to get the result
        result = longest_palindromic_substring(strings[i])
        # Print the result
        print("\t Number of palindromic substrings: ", result, sep="")
        # Print a horizontal line to separate the output
        print("-" * 100)


if __name__ == '__main__':
    main()

    
if __name__ == '__main__':
    main()