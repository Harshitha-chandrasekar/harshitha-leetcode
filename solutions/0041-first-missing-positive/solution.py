class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        store = set()
        for num in nums:
            if num>0:
                store.add(num)
        if not store:
            return 1
        mini = min(store)
        maxi = max(store)
        if mini!=1:
            return 1
        for i in range(mini,maxi):
            if i not in store:
                return i

        return maxi+1
