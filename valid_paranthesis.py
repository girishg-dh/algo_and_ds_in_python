def is_valid(s):
    open = ["(","{","["]
    close = [")","}","]"]
    stack = []
    match_found = False
    for ch in s:
        if ch in open:
            stack.append(ch)
        elif ch in close:
            if len(stack) == 0:
                return False
            if ch == ")" and stack[-1] == "(":
                stack.pop()
                match_found = True
            elif ch == "}" and stack[-1] == "{":
                stack.pop()
                match_found = True
            elif ch == "]" and stack[-1] == "[":
                stack.pop()
                match_found = True
            else:
                return False
    if len(stack) > 0:
        return False
    return True

def main():
    inputs = ["(){}[]", "{}[]{}[{}])", "(){[{()}]}", "))){{}}}]]", "{[()}"]

    for i in range(len(inputs)):
        print(i + 1, ". Input string = ", inputs[i], sep="")
        print("   Valid parentheses = ", is_valid(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()