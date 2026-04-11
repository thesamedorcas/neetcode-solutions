from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t= Counter (t)
     

        for i in s:
            if i not in t:
                return False
            
            if t[i]==0:
                return False
            
            t[i]-=1

        for i,v in t.items():
            if v!=0:
                return False
        return True

