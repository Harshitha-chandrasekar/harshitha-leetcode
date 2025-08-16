class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        newnum = num
        n = num
        c = 0
        while(num > 0):
            last = n % 10 ** c
            rest = n / 10 ** c
            if(rest%10 == 6):
                rest = rest//10
                newnum = ((rest*10 + 9)* (10**c)) + last
            c = c+1
            num = num //10

        return newnum
