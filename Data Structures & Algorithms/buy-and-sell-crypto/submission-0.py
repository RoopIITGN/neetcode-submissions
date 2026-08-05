class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b_l = prices[0]
        pr = 0
        for i in range(1, len(prices)):
            if(prices[i] > b_l):
                pr = max(pr, prices[i]-b_l)
            else:
                b_l = prices[i]
        return pr