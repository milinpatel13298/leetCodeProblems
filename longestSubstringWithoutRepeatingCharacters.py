class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength=0
        for i in range(len(s)):
            if maxLength>(len(s)-i):
                break
            longestSubstring=s[i]
            progressiveString=s[i+1:]
            for j in range(len(progressiveString)):
                if progressiveString[j] not in longestSubstring:
                    longestSubstring+=progressiveString[j]
                else:
                    break
            if len(longestSubstring)>maxLength:
                maxLength=len(longestSubstring)
        return maxLength
