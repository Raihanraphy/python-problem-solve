class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []

        for comb in combinations(range(1,10) , k):
            if sum(comb) == n:
                answer.append(list(comb))

        return answer
