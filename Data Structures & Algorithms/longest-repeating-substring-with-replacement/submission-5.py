class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        dict to keep track of letters where dict is <= lenght k
        check number of letter when see lteer if equals slide
        
        '''
        l=0

        track=dict()
        res=0
        m_f=0
        for r in range(len(s)):
            track[s[r]]= track.get(s[r], 0)+1

            m_f= max(m_f, track[s[r]])

            while (r-l+1) > m_f+k:
                track[s[l]]-=1
                l+=1
                

            res= max(res, r-l+1)


        return res