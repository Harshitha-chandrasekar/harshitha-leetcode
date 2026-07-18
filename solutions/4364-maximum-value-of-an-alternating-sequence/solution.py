class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n == 1:
            return s
            
        pairs = n//2

        return s + (m*pairs) - (pairs - 1)
