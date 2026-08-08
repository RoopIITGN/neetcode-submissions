from collections import deque
from heapq import heappush, heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        for i, val in enumerate(nums):
            while q and val>=nums[q[-1]]:
                q.pop()
            q.append(i)
            if(q[0] <= i-k):
                q.popleft()
            if(i >= k-1):
                res.append(nums[q[0]])
        return res