from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-ct for ct in counts.values()]
        heapq.heapify(max_heap)
        tm = 0
        q = deque()

        while(max_heap or q):
            tm += 1
            if(max_heap):
                ct = heapq.heappop(max_heap) + 1
                if(ct < 0):
                    q.append((ct, tm + n))
            
            if(q and q[0][1] == tm):
                ct, _ = q.popleft()
                heapq.heappush(max_heap, ct)

        return tm

