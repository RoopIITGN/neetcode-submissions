class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        counts = [0]*26

        for s_c, t_c in zip(s, t):
            counts[ord(s_c) - ord('a')] += 1
            counts[ord(t_c) - ord('a')] -= 1

        return all(ct == 0 for ct in counts)