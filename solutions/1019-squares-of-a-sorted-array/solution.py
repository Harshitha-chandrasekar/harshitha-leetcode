class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        left_ptr = 0
        right_ptr = n-1

        result_right = n-1

        while(left_ptr <= right_ptr):
            left_sq = nums[left_ptr] ** 2
            right_sq = nums[right_ptr] ** 2
            if(left_sq > right_sq):
                result[result_right] = left_sq
                left_ptr = left_ptr + 1
            else:
                result[result_right] = right_sq
                right_ptr = right_ptr -1
            result_right = result_right -1

        return result
