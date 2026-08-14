class Solution:
    # Good old valid parens
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)
            else:
                if stack:
                    # There are brackets to match
                    if stack[-1] == '(' and bracket ==')':
                        stack.pop()
                        continue
                    if stack[-1] == '{' and bracket =='}':
                        stack.pop()
                        continue
                    if stack[-1] == '[' and bracket ==']':
                        stack.pop()
                        continue
                    return False
                else: 
                    return False
        return not stack
                
                
        