class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue

            x = i+1
            y = len(nums)-1
            while x<y:
                total = nums[i]+nums[x]+nums[y]
                if total == 0:
                    ans.append([nums[i],nums[x],nums[y]])
                    x = x+1
                    y = y-1
                    while x<y and nums[x-1] == nums[x]:
                        x = x+1
                    while y>x and nums[y+1] == nums[y]:
                        y = y -1
                elif total<0:
                    x = x+1
                else:
                    y = y-1

        return ans
