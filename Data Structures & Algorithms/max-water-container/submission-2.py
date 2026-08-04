class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ar = 0
        l, r = 0, len(heights) - 1
        while(l < r):
            ar = max(ar, (min(heights[l], heights[r]) * (r-l)))
            if(heights[l] < heights[r]):  
                st = 1
                while(((l+st) < r) and (heights[l+st] <= heights[l])):
                    st += 1
                l += st
            else:
                st = 1
                while((l < (r-st)) and (heights[r-st] <= heights[r])):
                    st += 1
                r -= st
        return ar