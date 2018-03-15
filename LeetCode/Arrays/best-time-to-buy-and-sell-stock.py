import sys
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
        return 0

    max_profit = 0
    min_price = sys.maxsize
    for i in range(len(prices)):
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])

    return max_profit

print(maxProfit([7, 1, 5, 3, 6, 4]))