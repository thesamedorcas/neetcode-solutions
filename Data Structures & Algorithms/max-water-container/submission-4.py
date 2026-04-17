class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m_area= 0

        left= 0
        right =  len(heights)-1

        while left <right:
            length= min(heights[left], heights[right])
            width = right-left
            area= length*width
            m_area= max(m_area,area)
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
        return m_area

   


        