# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


from typing import List

"""
Sliding window :- two pointer technique is used

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,1                               #? setting up the pointer
        mProfit = 0

        while right < len(prices):                      #? checking whether the right pointer reaches the end of the list

            if prices[left] < prices[right]:            
                profit = prices[right] - prices[left]
                mProfit = max(profit,mProfit)           #? finding the maxprofit by subtracting the value in the right to the left
            else:
                left = right                            #? the left value is assigned to the right because in the else condition it means
                                                        #? right price is the lowest price currently available so setting the left price to the right
            right += 1
        
        return mProfit
    
result = Solution();
print(result.maxProfit([7,1,5,3,6,4]))