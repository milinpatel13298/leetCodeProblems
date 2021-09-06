class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        slowestDuration, durationI=0,0  #durationI will contain the duration of the key pressed for the ith iteration
        slowestKey=''
        for i in range(len(keysPressed)):
            #calculate durationI
            if i==0: durationI = releaseTimes[i]
            else: durationI = releaseTimes[i] - releaseTimes[i-1]
            #only proceed if durationI is longer (greater) than the current slowest duration
            if durationI>=slowestDuration:
                if durationI==slowestDuration:
                    #replace slowestKey if current key is lexicographically greater than the slowestKey
                    if slowestKey<keysPressed[i]:
                        slowestKey=keysPressed[i]
                        slowestDuration=durationI   #update slowestDuration value if slowestKEy has been replaced
                else:
                    slowestKey=keysPressed[i]
                    slowestDuration=durationI
        return slowestKey
