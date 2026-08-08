class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for2 = {}
        stack = []
        
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                idx = stack.pop()
                for2[nums2[idx]] = nums2[i]
            stack.append(i)

        ans = []
        for n in nums1:
            if n not in for2:
                ans.append(-1)
            else:
                ans.append(for2[n])

        return ans
