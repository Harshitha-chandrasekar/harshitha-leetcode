class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five >0:
                    five-=1
                    tens+=1
                else:
                    return False
            else:
                if tens>0 and five>0:
                    tens-=1
                    five-=1
                elif five>=3:
                    five-=3
                else:
                    return False

        return True
