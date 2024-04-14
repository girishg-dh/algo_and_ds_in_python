
def climb_stairs(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    lookup_table = [0] * (n+2)
    lookup_table[0] = 0
    lookup_table[1] = 1
    result = climb_stairs_iterative(n+1, lookup_table)
    print(lookup_table)
    return result

    

def climb_stairs_iterative(n, lookup_table):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if lookup_table[n] != 0:
        return lookup_table[n]
    lookup_table[n] = climb_stairs_iterative(n-1, lookup_table) + climb_stairs_iterative(n-2, lookup_table)
    return lookup_table[n]

#Driver code
def main():
    inputs = [5, 10, 30, 42, 6]
    
    for i in range(len(inputs)):
        print(i + 1, ".\t Steps: ",inputs[i],"\n\n\t", \
                         " Number of ways: ", climb_stairs(inputs[i]), sep="") 
            
        print("-" * 100)

if __name__ == '__main__':
    main()