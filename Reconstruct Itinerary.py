class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        # min-heap to get lexical order automatically
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)

        res = []

        def dfs(src):
            while adj[src]:
                nxt = heapq.heappop(adj[src])
                dfs(nxt)
            res.append(src)

        dfs("JFK")
        return res[::-1]
                


        
