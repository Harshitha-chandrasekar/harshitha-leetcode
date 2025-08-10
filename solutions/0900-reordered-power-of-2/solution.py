class Solution(object):

    def reorderedPowerOf2(self, n):
        # Extract digits
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10

        used = [False] * len(digits)

        # Backtracking to generate permutations
        def backtrack(path):
            if len(path) == len(digits):
                num = 0
                for d in path:
                    num = num * 10 + d
                return (num & (num - 1)) == 0
            for i in range(len(digits)):
                if used[i]:
                    continue
                if len(path) == 0 and digits[i] == 0:
                    continue  # skip leading zero
                used[i] = True
                if backtrack(path + [digits[i]]):
                    return True
                used[i] = False
            return False

        return backtrack([])

