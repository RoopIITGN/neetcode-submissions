from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        dct = {')':'(', '}':'{', ']':'['}
        
        for ch in s:
            if(ch in ['(','{','[']):
                stack.append(ch)
            elif(ch in [')','}',']']):
                if stack and stack[-1]==dct[ch]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return not stack