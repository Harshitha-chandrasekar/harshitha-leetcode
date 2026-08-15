class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        dictfriends = {}
        for i in range(len(friends)):
            dictfriends[i] = friends[i]

        dictwatched = {}
        for i in range(len(watchedVideos)):
            dictwatched[i] = watchedVideos[i]

        visited = set()
        visited.add(id)
        q = deque([[id]])
        while q and level>0:
            level -= 1
            levelf = []
            now = q.popleft()
            for dude in now:
                for friend in dictfriends[dude]:
                    if friend not in visited:
                        levelf.append(friend)
                        visited.add(friend)
            q.append(levelf)

        ansdict = {}
        for dude in q[0]:
            for video in dictwatched[dude]:
                if video in ansdict:
                    ansdict[video]+=1
                else:
                    ansdict[video]=1

        ans = sorted(ansdict.keys(), key=lambda video: (ansdict[video], video))
        return ans
