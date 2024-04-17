
def longest_palindromic_substring(string):
    """
    Function to find the length of the longest palindromic substring in a given string
    """
    # Create a 2D array to store the length of the longest palindromic substring
    # for each substring of the given string

    # Create a 2D array to store the length of the longest palindromic substring
    # for each substring of the given string
    length = len(string)
    if length < 2:
        return string
    dp = [[False] * length for _ in range(length)]

    start = 0
    max_len = 1

    # Base case when length of the string is 1
    for i in range(length):
        dp[i][i] = True
    
    # Check for substring of length 2
    for i in range(length - 1):
        if string[i] == string[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Main loop 
    # Start from size 3 to progrssively larger size 
    for size in range(3, length + 1):
        # Start sampling substrings from begining to string - size + 1
        for i in range(length - size + 1):
            # if i is start then end (j) is i + size - 1
            j = i + size - 1
            # check i and j are same or not
            # also if i+1 to j-1 is palindromic then i to j is also palindromic
            if string[i] == string[j] and dp[i+1][j-1]:
                dp[i][j] = True 
                start = i
                max_len = size
    # Return the length of the longest palindromic substring
    # Longest is will be of max_len and starts fron start
    return string[start: start + max_len]
        


# Driver code
def main():
    """
    Driver function to test the longest palindromic substring function
    """
    strings = ['cat', 'lever', 'xyxxyz', 'wwwwwwwwww', 'tattarrattat'],'"aabbccddccbbae"'
    
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