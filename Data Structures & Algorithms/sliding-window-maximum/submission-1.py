from heapq import heappush, heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if(k > len(nums)):
            return []
        max_heap = []
        res = []
        l = 0
        r = k-1
        store = {}
        for i in range(l, k):
            store[nums[i]] = store.get(nums[i], 0) + 1
            heappush(max_heap, -nums[i])
        
        mx = -heappop(max_heap)
        res.append(mx)
        # print(f"Outside = {res}")
        heappush(max_heap, -mx)
        for r in range(k, len(nums)):
            store[nums[r]] = store.get(nums[r], 0) + 1
            heappush(max_heap, -nums[r])
            c_l = nums[l]
            store[c_l] -= 1
            l += 1
            mx = -heappop(max_heap)
            while(mx == c_l) or (store[mx] == 0):
                if(store[mx]>0):
                    break
                else:
                    mx = -heappop(max_heap)           
            heappush(max_heap, -mx)
            res.append(mx)
        return res