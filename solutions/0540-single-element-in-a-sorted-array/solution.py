class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r = 0,len(nums)
        while l<r:
            m = (l+r)//2
            if m-1>=0 and nums[m-1] == nums[m]:
                llength = m-1
                if llength%2 == 1:
                    r = m-2
                else:
                    l = m+1

            elif m+1<len(nums) and nums[m+1] == nums[m]:
                llength = m
                if llength%2==1:
                    r = m-1
                else:
                    l = m+2


            else:
                return nums[m]

        return nums[l]
