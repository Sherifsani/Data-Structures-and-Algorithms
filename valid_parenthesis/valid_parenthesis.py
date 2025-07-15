class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) < 2:
            return False
        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            if c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            if c == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            if c == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
          
        return len(stack) == 0
            
