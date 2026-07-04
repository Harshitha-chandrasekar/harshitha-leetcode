class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            
            #if left issorted
            if nums[l]<=nums[m]:
                # if arr in that half
                if nums[l]<=target<=nums[m]:
                    r = m-1
                else:
                    l = m+1
            #is right is sorted
            else:
                #if t in that half
                if nums[m]<=target<=nums[r]:
                    l = m+1
                else:
                    r = m-1

        return -1
