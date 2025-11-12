class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        index_degree = [0] * numCourses

        for i, j in prerequisites:
            graph[i].append(j)
            index_degree[j] += 1
        
        q = deque([ i for i in range(numCourses) if index_degree[i] == 0])
        sorting = []
        while q:
            curr = q.popleft()
            sorting.append(curr)
            for i in graph[curr]:
                index_degree[i] -= 1
                if index_degree[i] == 0:
                    q.append(i)
        return len(sorting) == numCourses
