def calculator(expression: str) -> int:
    stack = []
    operators = ["+", "-"]
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    braces = ["(",")"]
    current_number = 0
    sign_value = 1
    result = 0
    for char in expression:
        if char in numbers:
            current_number = current_number * 10 + int(char)
        elif char in operators:
            result = result + current_number * sign_value
            current_number = 0
            sign_value = 1 if char == "+" else -1
        elif char in braces:
            if char == "(":
                stack.append(result)
                result = 0
                stack.append(sign_value)
                sign_value = 1
            else:
                result += sign_value * current_number
                current_number = 0
                result = result * stack.pop() + stack.pop()
    return result + sign_value * current_number


if __name__=="__main__":
    e1 = "(13+50)+(56-29-(7+2))"
    exprs = ["20 + (34 + 8 - (15 - 7) + 21) - 26", "(18 - 11 - (27 + 8 - 14) + 37)", "2183 - (612 + 499) + 137","4 + (52 - 12) + 99","(12 - 9 + 4) + ( 7 - 5)"]
    for e in exprs:
        print(calculator(e))