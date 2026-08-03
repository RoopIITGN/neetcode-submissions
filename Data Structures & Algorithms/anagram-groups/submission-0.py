class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rec = {}
        for s_i in strs:
            srt_i = "".join(sorted(s_i))
            if srt_i in rec:
                rec[srt_i].append(s_i)
            else:
                rec[srt_i] = [s_i]
        
        return list(rec.values())