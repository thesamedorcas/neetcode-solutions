class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track= {}

        for i in range(len(nums)):
            current= nums[i]
            complement= target-current

            if complement in track:
                return [track[complement], i]

            track[current]=i


        