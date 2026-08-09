class Solution:
    def maxProfit(self, prices):
        mini = prices[0]
        profit = 0

        for i in range(len(prices)):
            maxi = prices[i]
            mini = min(prices[i], mini)#  finds  small number form index 0 to present index
            profit = max(profit, maxi - mini)#  because we need profits from 0 only and i comapre previsou proft 
        return profit
    
# class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     maxi=0
    #     for i in range(len(prices)):
    #          for j in range(i,len(prices)):
    #              profit = prices[j]-prices[i]
    #              maxi=max(profit,maxi)
    #     return maxi

# Assume today is the selling day.
# Find the lowest buying price before today.
# Calculate profit.
# Keep the maximum profit.

# class Solution(object):
#     def maxProfit(self, prices):
#         min_price = prices[0]
#         max_profit= 0

#         for current in prices:

#             if current < min_price:
#                 min_price = current

#             temp = current - min_price

#             if temp > max_profit:
#                 max_profit= temp
#         return max_profit