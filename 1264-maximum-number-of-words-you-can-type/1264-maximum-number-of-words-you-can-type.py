class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words,c=text.split(" "),0
        for i in words:
            found=0
            for j in brokenLetters:
                if j in i:
                    found=1
                    break
            if found==0:
                c+=1
        return c