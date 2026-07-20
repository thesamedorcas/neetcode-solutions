class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= []
        storage= {}

        for i in strs:
            count= [0]*26
            for j in i:
                diff= ord(j) - ord('a')
                count[diff]+= 1
            count_tuple = tuple(count)
            if count_tuple in storage:
                storage[count_tuple].append(i)
            
            else:
                storage[count_tuple] = [i]

        for i,v in storage.items():
            res.append(v)
        return res

            

        
        
        