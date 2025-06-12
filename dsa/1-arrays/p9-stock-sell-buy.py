# Source: https://neetcode.io/problems/buy-and-sell-crypto?list=blind75
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Topic: Arrays
# Tags: tag1, tag2
# Related Concepts: ..
# Question: ..

class Solution:
    """
    T : O(n)
    S : O(1) 
    """

    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            profit_i = prices[i] - min_price

            max_profit = max(profit_i, max_profit)

            min_price = min(min_price, prices[i])

        return max_profit

    def maxProfit_two_pointers(self, prices: list[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP


# test cases
prices_1 = [7, 1, 5, 3, 6, 4]
prices_2 = [10, 1, 5, 6, 7, 40]

solution = Solution()

res = solution.maxProfit(prices_1)
print(res)


res = solution.maxProfit_two_pointers(prices_2)
print(res)
