class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        count = 0
        q = deque([beginWord])
        while q:
            count = count+1
            for _ in range(len(q)):
                n = q.popleft()
                if n == endWord:
                    return count
                for i in range(len(n)):
                    for c in range(97,123):
                        if chr(c) == n[i]:
                            continue
                        else:
                            newn = n[:i] + chr(c) + n[i+1:]
                            if newn in words:
                                q.append(newn)
                                words.remove(newn)

        return 0
