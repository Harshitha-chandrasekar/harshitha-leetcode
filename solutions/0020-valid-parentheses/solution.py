class Solution(object):
    def isValid(self, s):
        stack = []
        brackets = {'{': '}', '[': ']', '(': ')'}

        for ch in s:
            if ch in brackets:
                stack.append(ch)
            elif stack and ch == brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        if stack != []:
            return False
        return True

