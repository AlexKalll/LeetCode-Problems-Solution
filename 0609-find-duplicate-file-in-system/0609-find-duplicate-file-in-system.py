class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hT = defaultdict(list)

        for path in paths:
            dr = path.split()   

            # iterate over the paths after making them list
            for i in range(1, len(dr)):
                f = dr[i].split('(')
                n = len(f[-1]) # find the length of the file content 
                hT[f[-1][0:n-1]].append(dr[0]+ '/' +f[0])
                
        ans = []
        for txt in hT:
            if len(hT[txt]) > 1:
                ans.append(hT[txt])
        
        return ans