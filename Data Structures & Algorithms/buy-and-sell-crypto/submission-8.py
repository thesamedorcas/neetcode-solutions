class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first, *rest = prices
        max_diff= 0
        min_price= first

        for i in rest:
            current_diff= i-min_price
            max_diff= max(max_diff, current_diff)
            min_price= min(i, min_price)   

        return max_diff