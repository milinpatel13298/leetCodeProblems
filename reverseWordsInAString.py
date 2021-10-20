class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        answer=""
        word=""
        for i in s:
            if i is not " ":
                word+=i
            else:
                if word is not "":
                    answer=word+" "+answer
                    word=""
                else:
                    word=""
        answer=word+" "+answer
        return answer.strip()
