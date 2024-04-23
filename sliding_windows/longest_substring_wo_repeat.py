def find_longest_substring(string):
    """
    Function to find the length of the longest substring
    without repeating characters
    """
    char_map = dict()
    window_start = 0
    max_length = 0

    (start, end) = (0, 0)
    for idx in range(len(string)): # For each character in the string:
        if string[idx] not in char_map:
            char_map[string[idx]] = idx
        else:
            if char_map[string[idx]] >= window_start:
                window_start = char_map[string[idx]] + 1
                char_map[string[idx]] = idx
            else:
                char_map[string[idx]] = idx
        
        window_length = idx - window_start + 1
        if window_length > max_length:
            max_length, (start, end) = window_length, (window_start, idx)
    print("\tLongest substring: ", string[start:end + 1])
    return max_length
        

def main():
    string = [
        "abcabcbb",
        "pwwkew",
        "bbbbb",
        "ababababa",
        "",
        "ABCDEFGHI",
        "ABCDEDCBA",
        "AAAABBBBCCCCDDDD",
        "abccabcabcc"
    ]
    for i in range(len(string)):
        print(i + 1, ". \t Input String: ", string[i], sep="")
        print("\t Length of longest substring: ",
                (find_longest_substring(string[i])))
        print("-" * 100)


if __name__ == "__main__":
    main()