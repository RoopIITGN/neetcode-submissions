class Solution:
    def trap(self, height: List[int]) -> int:
        t_w, l, r = 0, 0, len(height) - 1
        l_m, r_m = height[l], height[r]
        while(l < r):
            if(l_m < r_m):
                l += 1
                l_m = max(l_m, height[l])
                t_w += (l_m - height[l])
            else:
                r -= 1
                r_m = max(r_m, height[r])
                t_w += (r_m - height[r])
        return t_w