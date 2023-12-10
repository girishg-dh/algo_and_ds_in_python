def myAtoi(s: str) -> int:
    MAX_INT = 2**31 -1
    MIN_INT = -2**31
    s = s.lstrip()
    first = True
    sign = 1
    result = 0
    runner = 0
    pointer = 0 
    while pointer < len(s):
        if result * sign > MAX_INT: return MAX_INT
        if result * sign < MIN_INT: return MIN_INT
        if first:
            if s[pointer] == "+" :
                first = False
                sign = 1
                pointer += 1
            elif s[pointer] == "-" :
                sign = -1
                pointer += 1
                first = False
        
        try:
            runner = int(s[pointer])
         #   ord()
            if first:
                result = runner
                first = False
            else:
                result = result * 10 + runner
            pointer += 1
        except:
            return result * sign
    return result * sign
def main():
    print(myAtoi("79"))
    print(myAtoi("king 25"))
    print(myAtoi("-33"))
    print(myAtoi("-91283472332"))
    print(myAtoi("91283472332")) 

if __name__ == '__main__':
    main()


