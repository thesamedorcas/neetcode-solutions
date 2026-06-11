class Solution:
    def isValid(self, s: str) -> bool:

        stack= []

        match= {')': '(','}':'{', ']': '['}


        for i in s:
            if stack and i in match:
                if stack[-1]== match[i]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(i)
    
        return len(stack)==0
