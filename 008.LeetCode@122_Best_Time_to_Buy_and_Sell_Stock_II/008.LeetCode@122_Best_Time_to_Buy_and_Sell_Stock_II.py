class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max=0
        start=prices[0]
        for price in prices:
            if start<price:
                max+=price-start
            start=price
        return max