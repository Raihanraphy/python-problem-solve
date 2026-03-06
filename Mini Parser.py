
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        a = json.loads(s)
        return self.dfs(a)

    def dfs(self, input) -> NestedInteger:
        if isinstance(input, int):
            return NestedInteger(input)
        l = NestedInteger()
        for e in input:
            l.add(self.dfs(e))
        return l
