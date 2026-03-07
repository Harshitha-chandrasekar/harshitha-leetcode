class Solution(object):
    def minFlips(self, s):
        n = len(s)
        news = s + s
        diff1 = 0
        diff2 = 0

        for i in range(n):
            if news[i] != ('0' if i % 2 == 0 else '1'):
                diff1 += 1
            if news[i] != ('1' if i % 2 == 0 else '0'):
                diff2 += 1
        
        ans = min(diff1, diff2)

        for i in range(n, 2 * n):
            if news[i] != ('0' if i % 2 == 0 else '1'):
                diff1 += 1
            if news[i] != ('1' if i % 2 == 0 else '0'):
                diff2 += 1

            left_idx = i - n
            if news[left_idx] != ('0' if left_idx % 2 == 0 else '1'):
                diff1 -= 1
            if news[left_idx] != ('1' if left_idx % 2 == 0 else '0'):
                diff2 -= 1

            ans = min(ans, diff1, diff2)

        return ans
