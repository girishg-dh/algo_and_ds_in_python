def add_binary(str1: str, str2: str) -> str:
    result = ""
    str1, str2 = str1[::-1], str2[::-1]
    carry = 0
    max_length = max(len(str1), len(str2))
    for index in range(max_length):
        if index < len(str1):
            i = str1[index]
        else:
            i = "0"
        if index < len(str2):
            j = str2[index]
        else:
            j = "0"

        flag = int(i) + int(j)
        if flag == 2:
            if carry > 0:
                result += "1"
            else:
                result += "0"
            carry = 1
        elif flag == 1:
            if carry > 0:
                result += "0"
            else:
                result += "1"
        else:
            if carry > 0:
                result += "1"
                carry = 0
            else:
                result += "0"
                carry = 0
    if carry > 0:
        result += "1"
    return result[::-1]


print(add_binary("1","1"))