class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != stones[0]+1:
            return False
        n=len(stones)
        maxDistance, maxJump = n*(n+1)/2, n
        minDistance = n-1
        if maxDistance<stones[-1] or minDistance>stones[-1]:
            return False
        stonesSet = set(stones)
        # jump
        @cache
        def backtrack(currLocation, jump):
            # check if we at the end
            if currLocation == stones[-1]:
                return True
            # try to move
            for possibleJump in range(jump+1, max(jump-1,1)-1, -1):
                # check state
                if currLocation+possibleJump in stonesSet:
                    if backtrack(currLocation+possibleJump, possibleJump):
                        return True
                # fail, backtrack
        if backtrack(stones[1], 1):
            return True
        return False
