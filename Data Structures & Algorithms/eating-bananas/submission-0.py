class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if(h == len(piles)):
            return max(piles)
        l, r = 1, max(piles)
        res = r
        while(l <= r):
            m = (l+r)//2
            c_h = sum(math.ceil(i/m) for i in piles)
            # print(f"l = {l}, r = {r}, m = {m}, c_h = {c_h}")
            if(c_h > h):
                l = m+1
            elif(c_h <= h):
                res = m
                r = m-1
        return res