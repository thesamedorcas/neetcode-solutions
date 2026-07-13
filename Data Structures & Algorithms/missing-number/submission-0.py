class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        esum= n*(n+1)//2
        currsum= sum(nums)

        return esum-currsum
        