# Time : O(n)
# Memory: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
##using two pointers to get the difference and taking out max from 
        left,right = 0,1
        maxPrice = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxPrice = max(maxPrice,profit)
            else:
                left = right
            right += 1
        return maxPrice
            
