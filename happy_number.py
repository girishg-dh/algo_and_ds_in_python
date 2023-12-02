def is_happy_number(n):
    slow = n
    fast = squared_sum(n)
    if fast == 1:
        return True
    while fast != slow:
        if fast == 1:
            return True
        else:
            if fast == slow:
                return False
            else:
                slow = squared_sum(slow)
                #print("slow : ", slow)
                fast = squared_sum(squared_sum(fast))
                #print("fast: ", fast)
    return False



def squared_sum(n):
    sum = 0
    while n > 0:
        digit = n % 10 
        sum += digit**2
        n = n // 10
    return sum


if __name__=="__main__":
    print(is_happy_number(7))
   # print(is_happy_number(1))