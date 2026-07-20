class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        t= set(nums)
        res=0
        for i in nums:
            
            count= 0
            curr= i

            while curr in t:
                count+=1
                curr+=1
            res= max(count, res)

        return res


        