class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        slowestDuration, durationI=0,0
        slowestKey=''
        for i in range(len(keysPressed)):
            if i==0: durationI = releaseTimes[i]
            else: durationI = releaseTimes[i] - releaseTimes[i-1]
            if durationI>=slowestDuration:
                if durationI==slowestDuration:
                    if slowestKey<keysPressed[i]:
                        slowestKey=keysPressed[i]
                        slowestDuration=durationI
                else:
                    slowestKey=keysPressed[i]
                    slowestDuration=durationI
        return slowestKey
