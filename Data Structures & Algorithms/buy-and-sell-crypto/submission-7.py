class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_diff = 0

        for i in prices[1:]:
            curr_diff = i - min_price
            max_diff = max(curr_diff, max_diff)
            min_price = min(min_price, i)

        return max_diff
