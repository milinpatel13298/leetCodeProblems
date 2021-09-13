class Solution:
    """
    def shift(self,x: str, n: int) -> str:
        alphabets='abcdefghijklmnopqrstuvwxyz'
        return alphabets[(ord(x)-ord('a')+n)%26]
    """
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        answer=''
        alphabets='abcdefghijklmnopqrstuvwxyz'
        for i in range(len(s)):
            #answer+=self.shift(s[i],(sum(shifts[i:])%26))
            answer+=alphabets[(ord(s[i])-ord('a')+(sum(shifts[i:])%26))%26]
        return answer
