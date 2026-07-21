class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        m_set= set()

        l=0
        res=0
        for r in range(len(s)):
            if s[r] in m_set:
                while s[r] in m_set:
                    m_set.remove(s[l])
                    l+=1
        
            m_set.add(s[r])
            
            res= max(res, len(m_set))

        return res