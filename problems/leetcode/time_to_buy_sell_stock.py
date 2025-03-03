# kadane's algorithm

def maxProfit(prices):
    count = 0
    maxProfit = 0
    for i in range(1, len(prices)):
        if prices[count] > prices[i]:
            count = i
        elif maxProfit < prices[i] - prices[count]:
            maxProfit = prices[i] - prices[count]
        else:
            continue

    return maxProfit


print(maxProfit([7, 1, 5, 3, 6, 4]))
