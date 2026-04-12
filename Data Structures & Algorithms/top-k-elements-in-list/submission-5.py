class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count= {}
        freq= [[] for i in range(len(nums))]

        for i in nums:
            count[i]=count.get(i, 0)+1

        for key, val in count.items():
            freq[val-1].append(key)

        result=[]
        for i in range(len(freq)-1, -1, -1):
                if freq[i]:
                    for j in freq[i]:
                        if len(result)< k:
                            result.append(j)
                        else:
                            return result
                    
        return result



        
        