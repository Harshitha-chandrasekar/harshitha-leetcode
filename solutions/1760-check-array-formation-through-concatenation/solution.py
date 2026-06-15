class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        mapping = {piece[0]: piece for piece in pieces}
        
        res = []
        for num in arr:
            if num in mapping:
                res.extend(mapping[num])
                
        return res == arr
