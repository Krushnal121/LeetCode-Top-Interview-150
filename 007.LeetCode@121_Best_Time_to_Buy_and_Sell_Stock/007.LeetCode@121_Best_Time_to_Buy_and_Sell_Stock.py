class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevlow=prices[0]
        maxout=0
        for price in prices:
            prevlow=min(price,prevlow)
            maxout=max((price-prevlow),maxout)
        return maxout