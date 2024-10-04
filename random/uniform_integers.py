# Write any import statements here

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    count = 0
    for d in range(1, 10):
        counter = d
        while counter <= B:
            if A <= counter <= B:
                count += 1
            counter = counter * 10 + d
    return count



print(getUniformIntegerCountInInterval(75, 300))
print(getUniformIntegerCountInInterval(1, 9))
print(getUniformIntegerCountInInterval(999999999999, 999999999999))