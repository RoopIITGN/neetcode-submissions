class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ln = len(temperatures)
        res = [0] * ln
        for i in range(ln-2, -1, -1):
            cur_tmp = temperatures[i]
            nxt = i+1
            while(nxt<ln and cur_tmp>=temperatures[nxt]):
                if(res[nxt] == 0):
                    nxt = ln
                    break
                nxt += res[nxt]

            if(nxt<ln):
                res[i] = nxt - i
        return res