class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        strg = {}
        for i in nums:
            if i in strg:
                strg[i] += 1
            else:
                strg[i] = 1
        
        heap = []
        for num, freq in strg.items():
            heapq.heappush(heap, (freq, num))
            if(len(heap) > k):
                heapq.heappop(heap)
        
        return [num for freq, num in heap]