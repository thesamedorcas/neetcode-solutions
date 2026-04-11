class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        md= {}

        for i, v in enumerate(nums):
            diff = target-v

            if diff in md:
                return [md[diff], i]
            md[v]= i
        
        