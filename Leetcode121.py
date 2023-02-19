class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        maximum = prices[l]
        maxprofit = 0

        while l<r and r<len(prices):
            
            if prices[l] < prices[r]:
                print(prices[r],prices[l])
                profit = prices[r] - prices[l]
                maxprofit = max(profit,maxprofit)
                r +=1
            
            else:
                l = r
                r += 1
         
        return maxprofit
