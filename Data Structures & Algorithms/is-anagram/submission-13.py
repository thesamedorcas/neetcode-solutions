from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict= Counter(s)# O(N) space

        for i in t: #o(n) LOOP
            if i not in s_dict:
                return False
            else:
                s_dict[i]-=1
        
        for j in s_dict:
            if s_dict[j]!=0:
                return False

        return True
            
            


        