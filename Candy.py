class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        if n<=1:
            return n
        candies=1
        up=down=peak=0
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                up+=1
                peak=up
                candies+=1+up
                down=0
            elif ratings[i]==ratings[i-1]:
                up=down=peak=0
                candies+=1
            else:
                up=0
                down+=1
                candies+=1 + down-(1 if down<=peak else 0)
        return candies
