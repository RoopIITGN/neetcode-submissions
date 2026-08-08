class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if(i in ['+','-','*','/']):
                scd = int(stack.pop())
                fst = int(stack.pop())
                if i == '+':
                    stack.append(str(fst + scd))
                elif i == '-':
                    stack.append(str(fst - scd))
                elif i == '*':
                    stack.append(str(fst * scd))
                else:
                    stack.append(str(int(fst / scd)))
            else:
                stack.append(i)

        return int(stack[0])