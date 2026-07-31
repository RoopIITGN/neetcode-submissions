class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        counts = [0]*26

        for s_c in s:
            counts[ord(s_c) - ord('a')] += 1
        for t_c in t:
            i = ord(t_c) - ord('a')
            if counts[i] == 0:
                return False
            counts[i] -= 1

        return all(ct == 0 for ct in counts)