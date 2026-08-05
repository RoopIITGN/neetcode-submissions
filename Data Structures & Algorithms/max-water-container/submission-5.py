class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ar = 0
        l, r = 0, len(heights) - 1
        while(l < r):
            c_ar = min(heights[l], heights[r]) * (r-l)
            if(c_ar > ar):
                ar = c_ar
            if(heights[l] < heights[r]):  
                prev = l
                for l in range(prev+1, r+1):
                    if(heights[l] > heights[prev]):
                        break
            else:
                prev = r
                for r in range(prev-1, l-1, -1):
                    if(heights[r] > heights[prev]):
                        break
        return ar