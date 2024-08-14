# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

from typing import List

"""
In this method i had used the same idea of question number 121

here we can make as many transactions but can only use the stock one time
"""
class MySolution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        maxP = 0

        while r < len(prices):

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = maxP+profit                              #? Profit is added to the variable and else condition is not used
                                                                #? Increment both pointer 
            l = r     
            r += 1
        
        return maxP
    
result = MySolution()
print(result.maxProfit([7,1,5,3,6,4]))


#! NeetCode Solution

"""
Here two pointer method is not used

it is checking the previous value and adding the profit to it.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 

        for i in range(1,len(prices)):

            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1] )

        return profit 
    
result = Solution()
print(result.maxProfit([7,1,5,3,6,4]))