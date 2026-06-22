class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for w in strs:
            sorteds = ''.join(sorted(w))
            res[sorteds].append(w)
        return list(res.values())
