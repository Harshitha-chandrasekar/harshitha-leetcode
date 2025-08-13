class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m
        j = n
        k = m + n
        while i>0 and j>0:
            if(nums1[i-1]> nums2[j-1]):
                nums1[k-1] = nums1[i-1]
                i = i-1
            else:
                nums1[k-1] = nums2[j-1]
                j = j-1
            k = k-1

        while j>0:
            nums1[k-1] = nums2[j-1]
            j = j-1
            k = k-1

