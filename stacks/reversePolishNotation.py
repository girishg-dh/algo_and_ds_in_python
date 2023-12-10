def rpn(tokens: list)-> int:
    stack = []
    operators = ["+","-","*","/"]
    result = 0
    for c in tokens:
        if c in operators:
            a, b = stack.pop(), stack.pop()
            if c == "+":
                result =  b+a
            elif c == "-":
                result =  b-a
            elif c =="*":
                result =  b*a
            elif c =="/":
                result =  b/a
            stack.append(int(result))
        else:
            stack.append(int(c))
    return stack.pop()


token1 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

print(rpn(token1))