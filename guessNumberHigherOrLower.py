# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        foundAnswer=False
        low,high=1,n
        while(not foundAnswer):
            current=(low+high)//2
            #result=guess(current)
            if guess(current) == 0:
                foundAnswer=True
            elif  guess(current) < 0:
                high=current-1
            else:
                low=current+1
        return current
