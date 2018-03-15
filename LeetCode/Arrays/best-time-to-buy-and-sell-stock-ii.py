'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
'''
def maxProfit(prices):
    if len(prices)<2:
        return 0
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i]>prices[i-1]:
            max_profit+=prices[i]-prices[i-1]
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))