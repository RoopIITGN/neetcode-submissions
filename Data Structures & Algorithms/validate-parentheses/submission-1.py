from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        q = deque()
        valid = False
        for ch in s:
            if(ch in ['(','{','[']):
                q.append(ch)
            elif(ch in [')','}',']']):
                if q:
                    pp = q.pop()
                    if(ch==')' and pp=='('):
                        continue
                    elif(ch=='}' and pp=='{'):
                        continue
                    elif(ch==']' and pp=='['):
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                return False
        if q:
            return False
        else:
            return True