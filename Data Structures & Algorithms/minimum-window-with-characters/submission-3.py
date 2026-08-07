class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or (len(s)<len(t)):
            return ""
        t_count = Counter(t)
        have, need = 0, len(t_count)
        sub, m_len = [-1, 1], float("inf")
        s_count = {}
        l = 0
        for r, ch in enumerate(s):
            # print(f"Inside for loop, r = {r}")
            if ch in t_count:
                s_count[ch] = s_count.get(ch, 0) + 1
                if(s_count[ch] == t_count[ch]):
                    have += 1
                # print(f"s_count = {s_count}")
                while(have == need):
                    # print(f"Entered while, with {s[l:r+1]}")            
                    c_len = r-l+1
                    if(c_len < m_len):
                        sub = [l, r]
                        m_len = c_len
                        # print(f"m_len = {m_len}")
                    if(s[l] in s_count):
                        s_count[s[l]] -= 1
                        if(s_count[s[l]] < t_count[s[l]]):
                            have -= 1
                        
                    l += 1

        l, r = sub
        if(m_len < float("inf")):
            return s[l:r+1]
        else:
            return ""
                
