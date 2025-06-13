class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        def check(x,y,t):
            if x>=0 and y>=0 and x<row and y<col and (x,y,t) not in visited:
                return True
            return False
        
        row,col=len(grid),len(grid[0])
        visited=set()
        
        def dfs(r,c,t):
            if check(r,c,t):
                visited.add((r,c,t))
                if t==1:
                    dfs(r,c+1,3)# going right
                elif t==2:
                    dfs(r+1,c,0)# going down
                elif t==3:
                    dfs(r,c-1,1) # going back
                elif t==0: 
                    dfs(r-1,c,2)# going up
                if grid[r][c]!="/":
                    dfs(r,c,t^1) #trick to traverse 0 to 1 or 3 to 2 and viceversa
                if grid[r][c]!="\\":
                    dfs(r,c,t^3)#trick to traverse 3 to 0 or 1 to 2 and viceversa
        
        cntofregion=0
        for i in range(row):
            for j in range(col):
                for typ in range(4):
                    if (i,j,typ) not in visited:
                        dfs(i,j,typ)
                        cntofregion+=1
        return cntofregion                
        