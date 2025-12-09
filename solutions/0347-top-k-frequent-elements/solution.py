class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1

        N = len(nums)
        buckets = [[] for _ in range(N + 1)] 

        for num, count in freq.items():
            buckets[count].append(num)

        result = []
        for i in range(N, 0, -1):
            if buckets[i]:
                result.extend(buckets[i]) 
                
                if len(result) >= k:
                    return result[:k] 
                    
        return result[:k]
