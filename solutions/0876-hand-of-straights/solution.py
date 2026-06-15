class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        n = len(hand)
        hand.sort()
        if n%groupSize!=0:
            return False

        while hand:
            c = hand[0]
            i = 0
            while i<groupSize:
                if c in hand:
                    hand.remove(c)
                    c = c+1
                    i = i+1
                else:
                    return False

        return True
