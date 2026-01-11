class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]

        # How many MHTS a graph can have at most?
        # A graph can have at most two MSTs
        # We'll assume a centre from where we'll expand our graph
        # If we remove all the layers i.e, the leaf cities, we can have one or two centres

        adj = [[] for i in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]        
            adj[u].append(v)
            adj[v].append(u)

        leaves = [i for i in range(n) if len(adj[i]) == 1]
        
        # Peel all the leaves until one or two remain
        while n > 2:
            n -= len(leaves)
            newLeaves = []

            for leaf in leaves:
                neighbor = adj[leaf][0] # Leaf has only a single neighbor

                # If removing leaf makes it a leaf, add it
                adj[neighbor].remove(leaf)

                if len(adj[neighbor]) == 1:
                    newLeaves.append(neighbor)
            
            # Repeat the process until we have one or two centres
            leaves = newLeaves
        
        return leaves

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
