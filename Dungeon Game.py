class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        r= len(dungeon)
        c= len(dungeon[0])

        soln= [[0]*c for i in range(r)]
        soln[r-1][c-1]= 1 if dungeon[r-1][c-1]>0 else (1- dungeon[r-1][c-1])

        for i in range(r-2, -1, -1):
            soln[i][c-1]= max(soln[i+1][c-1]- dungeon[i][c-1], 1)
        
        for j in range(c-2, -1, -1):
            soln[r-1][j]= max(soln[r-1][j+1] - dungeon[r-1][j], 1)

        for i in range(r-2, -1, -1):
            for j in range(c-2, -1, -1):
                soln[i][j]= max(min(soln[i+1][j], soln[i][j+1])- dungeon[i][j], 1)

        return soln[0][0]
