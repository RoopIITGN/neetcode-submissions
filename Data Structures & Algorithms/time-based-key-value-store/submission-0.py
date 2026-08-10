from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        vals = self.store[key]
        l, r = 0, len(vals)-1
        while(l <= r):
            m = (l+r)//2
            m_t, m_v = vals[m]
            if(m_t > timestamp):
                r = m-1
            else:
                res = m_v
                l = m+1
        return res
