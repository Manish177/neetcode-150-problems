class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        op=['+', '-', '*', '/']
        temp=0
        for i in tokens:
            if i not in op:
                 stk.append(int(i))
            else:
                val1=stk.pop()
                val2=stk.pop()
                if i=='+':
                    temp=val2+val1
                    stk.append(temp)
                if i=='-':
                    temp=val2-val1
                    stk.append(temp)
                if i=='*':
                    temp=val2 * val1
                    stk.append(temp)
                if i=='/':
                    temp=int(val2 / val1)
                    stk.append(temp)
        return stk.pop()