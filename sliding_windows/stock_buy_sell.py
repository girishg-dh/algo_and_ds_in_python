def max_profit(prices):
    max_profit = 0
    buy_index, sell_index = 0, 0
    buy_price = prices[buy_index]
    while sell_index < len(prices):
        sell_price = prices[sell_index]
        if buy_price > sell_price:
            buy_index = sell_index
            buy_price = prices[buy_index]
        max_profit = max(max_profit, sell_price - buy_price)
        sell_index += 1
    return max_profit




def main():
    prices = [
                [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9],
                [8, 2, 6, 4, 7, 5],
                [7, 6, 4, 3, 1],
                [2, 6, 8, 7, 8, 7, 9, 4, 1, 2, 4, 5, 8],
                [1, 2]
             ]

    for i in range(len(prices)):
        print(i + 1, ". Stock prices = ", prices[i], sep="")
        print("   Maximum profit = ", max_profit(prices[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()