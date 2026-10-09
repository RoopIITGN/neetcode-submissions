from collections import Counter, heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        max_count = sum(1 for v in counts.values() if v == max_freq)
        framework_time = (max_freq - 1) * (n + 1) + max_count
        return max(framework_time, len(tasks))
