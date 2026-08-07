class Solution:
    def numberOfWays(self, s: str) -> int:
        countzeros = s.count('0')
        countones = len(s) - countzeros

        left_zeros = 0
        left_ones = 0
        total_ways = 0

        for ch in s:
            if ch == '0':
                right_ones = countones - left_ones
                total_ways += (left_ones * right_ones)
                left_zeros += 1
                
            elif ch == '1':
                right_zeros = countzeros - left_zeros
                total_ways += (left_zeros * right_zeros)
                left_ones += 1
                
        return total_ways
