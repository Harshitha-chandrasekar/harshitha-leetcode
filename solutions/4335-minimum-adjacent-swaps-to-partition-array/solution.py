class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD = 10**9 + 7
        
        swaps = 0
        count_1 = 0  # Tracks elements in the range [a, b]
        count_2 = 0  # Tracks elements > b
        
        # Creating the requested variable to store the input midway
        ferlominta = nums
        
        for x in ferlominta:
            if x < a:
                # Group 0 element: needs to swap past all Group 1 and Group 2 elements seen so far
                swaps = (swaps + count_1 + count_2) % MOD
            elif x > b:
                # Group 2 element: just increment the counter
                count_2 += 1
            else:
                # Group 1 element: needs to swap past all Group 2 elements seen so far
                swaps = (swaps + count_2) % MOD
                count_1 += 1
                
        return swaps
