class Solution(object):
    def reverse(self, x):
        if x< 0:
            y = -x
        else:
            y = x
        z = 0
        while y>0:
            z = z*10 + y%10
            y = y/10

        if (z<-2**31) or (z> (2**31 -1)):
            return 0
        elif x<0:
            return -z
        else:
            return z
        
