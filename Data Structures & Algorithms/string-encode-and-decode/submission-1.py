class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s_i in strs:
            res += str(len(s_i))
            res += '#'
            r_i = ""
            for c in s_i:
                c_n = (ord(c) + 10) % 256
                r_i += chr(c_n)
            res += r_i       
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        cur = 0
        while(cur < len(s)):
            fwd = cur + 1
            while(s[fwd] != '#'):
                fwd += 1
            ln = int(s[cur:fwd])
            cur = fwd + 1
            stg = s[cur : cur + ln]
            r_i = ""
            for c_i in stg:
                c_n = ord(c_i) - 10
                if(c_n < 0):
                    c_n += 256
                r_i += chr(c_n)
            res.append(r_i)
            cur = cur + ln
        return res
