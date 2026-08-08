class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {']':'[',
                        '}':'{',
                        ')':'('}

        for c in s:
            if c in dictionary.values():
                stack.append(c)
            else:
                if not stack:
                    return False
                if dictionary[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False
