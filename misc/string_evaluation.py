"""
Statement
Given a string containing an arithmetic expression, implement a basic calculator that evaluates the expression string. The expression string can contain integer numeric values and should be able to handle the “+” and “-” operators, as well as “()” parentheses.

Constraints:

Let s be the expression string. We can assume the following constraints: 
s consists of digits, “+”, “-”, “(”, and “)”.
s represents a valid expression.
“+” is not used as a unary operation (+1 and +(2+3) +(2+3) are invalid).
“-” could be used as a unary operation (−1−1 and −(2+3) −(2+3)are valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""
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


# Driver code
def main():
    global DBG
    input = (
             "4 + (52 - 12) + 99",
             "(31 + 7) - (5 - 2)",
             "(12 - 9 + 4) + ( 7 - 5)",
             "8 - 5 + (19 - 11) + 6 + (10 + 3)",
             "56 - 44 - (27 - 17 - 1) + 7"
            )

    num = 1
    for i in input:
        # Set to False to supress line-by-line trace
        DBG = True
        print(num, ".", "\tGiven Expression: ", i, sep="")
        if DBG:
            print("\n\t\tProcessing...")
        print("\tThe result is: ", calculator(i))
        num += 1
        print("-"*100, sep="")


if __name__ == "__main__":
    main()
