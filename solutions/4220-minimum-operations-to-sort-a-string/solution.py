class Solution:
    def minOperations(self, s: str) -> int:
        
        if s == ''.join(sorted(s)):
            return 0

        if len(s) == 2:
            return -1

        if s[0] == min(s) or s[-1] == max(s):
            return 1

        if s[0] == max(s) and s[-1] == min(s):
            if max(s) in s[1:-1] or min(s) in s[1:-1]:
                return 2
            return 3

        return 2

