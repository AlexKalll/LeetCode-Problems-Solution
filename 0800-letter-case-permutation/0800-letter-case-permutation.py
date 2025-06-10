class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output=[""] #
        for i in s:
            tmp=[]
            if i.isalpha():
                for j in output:
                    tmp.append(j+i.lower())
                    tmp.append(j+i.upper())
            else:
                for j in output:
                    tmp.append(j+i)
            output=tmp
        return output
        