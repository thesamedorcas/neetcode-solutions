import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums= nums
        heapq.heapify(nums)
        self.k= k
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)

        

    def add(self, val: int) -> int:
        if len(self.nums) == self.k and val <= self.nums[0]:
            return self.nums[0]
        heapq.heappush(self.nums, val)
        if len(self.nums)>self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
        
        
