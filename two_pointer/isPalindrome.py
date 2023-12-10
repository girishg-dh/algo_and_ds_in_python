def is_palindrome(s:str)-> bool:
    l, r = 0, len(s) - 1
    while(l < r):
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
    return True


def main():
    print(is_palindrome("ABCDABCD"))
    print(is_palindrome("kayak"))
    print(is_palindrome("hellp"))
    print(is_palindrome("RACECAR"))
    print(is_palindrome("A"))



if __name__ == '__main__':
    main()