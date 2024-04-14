

def coin_change(coins: list, total: int) -> int:
    counter = [float('inf')] * total
    if total < 1:
        return 0
    result = coin_change_recursive(coins, total, counter)
    return result


def coin_change_recursive(coins: list, total: int, counter):
    if total < 0:
        return -1 
    if total == 0:
        return 0
    if counter[total - 1] != float('inf'):
        return counter[total - 1]
    minimum = float('inf')

    for coin in coins:
        result = coin_change_recursive(coins, total - coin, counter)
        if result >= 0 and result < minimum:
            minimum = 1 + result
    counter[total - 1] = minimum if minimum != float('inf') else -1
    return counter[total-1]





# Driver Code

def main():

    coins = [[1, 3, 4, 5], [1, 4, 6, 9], [6, 7, 8], [1, 2, 3, 4, 5], [14, 15, 18, 20],[10,20]]
    total = [7, 11, 27, 41, 52, 15]

    for i in range(len(total)):
        print(str(i+1) + ".\tThe minimum number of coins required to find " + str(total[i]) + " from " + str(coins[i]) + " is: " + str(coin_change(coins[i], total[i])))
        print("-" * 100)

if __name__ == '__main__':
    main()