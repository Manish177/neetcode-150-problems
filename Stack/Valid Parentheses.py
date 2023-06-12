class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={'(': ')','[': ']','{': '}'}
        for i in s:
            if i in pairs:
                stack.append(i)
                continue
            if i in pairs.values() and len(stack)<1:
                return False

            else:
                if pairs[stack[-1]]==i:
                    stack.pop()
                else:
                    return False

        if len(stack)==0:
            return True