def word_break(s, word_dict):
    """
    :type s: str
    :type word_dict: List[str]
    :rtype: bool
    """
    n = len(s)
    dp = [False] * (n+1)
    dp[0] = True
    for i in range(1, n+1):
        for j in range(i):
            if s[j:i] in word_dict:
                if dp[j] == True:
                    dp[i] = True
                    break
    return dp[n]

# Driver Code
def main():

    s = ["vegancookbook", "catsanddog", "highwaycrash",
         "pineapplepenapple", "screamicecream", "educativecourse"]
    word_dict = ["ncoo", "kboo", "inea", "icec", "ghway", "and", "anco", "hi", "way", "wa",
                 "amic", "ed", "cecre", "ena", "tsa", "ami", "lepen", "highway", "ples",
                 "ookb", "epe", "nea", "cra", "lepe", "ycras", "dog", "nddo", "hway",
                 "ecrea", "apple", "shp", "kbo", "yc", "cat", "tsan", "ganco", "lescr",
                 "ep", "penapple", "pine", "book", "cats", "andd", "vegan", "cookbook"]

    print("The list of words we can use to break down the strings are:\n\n", word_dict, "\n")
    print("-" * 100)
    for i in range(len(s)):
        print("Test Case #", i+1, "\n\nInput: '" + str(s[i])+"'\n")
        print_possible_combinations(s[i], word_dict)
        print("\nOutput: " + str(word_break(str(s[i]), word_dict)))
        print("-" * 100)

def print_possible_combinations(s, word_dict):
    print("The possible combinations are:\n")
    for i in range(len(word_dict)):
        if word_dict[i] in s:
            print(word_dict[i])


if __name__ == '__main__':
    main()