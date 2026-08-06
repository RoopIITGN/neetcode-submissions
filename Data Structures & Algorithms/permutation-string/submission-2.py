class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) == 0) or (len(s2) == 0) or (len(s1)>len(s2)):
            return False
        d_s1 = [0]*26
        d_s2 = [0]*26
        for i in range(len(s1)):
            d_s1[ord(s1[i]) - ord('a')] += 1
            d_s2[ord(s2[i]) - ord('a')] += 1
        if(d_s1 == d_s2):
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            d_s2[ord(s2[r]) - ord('a')] += 1
            d_s2[ord(s2[l]) - ord('a')] -= 1
            if(d_s1 == d_s2):
                return True
            l += 1
        return False


