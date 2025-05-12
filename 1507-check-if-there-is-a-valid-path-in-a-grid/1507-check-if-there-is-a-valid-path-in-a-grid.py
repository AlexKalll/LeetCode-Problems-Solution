class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        drs = {1:[(0,-1),(0,1)],2:[(1,0),(-1,0)],3:[(0,-1),(1,0)],
                    4:[(0,1),(1,0)],5:[(0,-1),(-1,0)],6:[(0,1),(-1,0)]}
        q = deque()
        visited = set()
        q.append((0,0))
        visited.add((0,0))
        
        while q:
            x,y=q.popleft()
            if x == rows-1 and y == cols-1:
                return True
            for dx,dy in drs[grid[x][y]]:
                next_x = x + dx
                next_y = y + dy
                if 0 <= next_x < rows and 0 <= next_y < cols and (next_x,next_y) not in visited:
                    if (-dx,-dy) in drs[grid[next_x][next_y]]:
                        q.append((next_x,next_y))
                        visited.add((next_x,next_y))
        return False