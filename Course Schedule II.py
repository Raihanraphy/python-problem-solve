from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        course_list = defaultdict(list)
        course_in_degrees = [0] * numCourses
        for cur, pre in prerequisites:
            course_list[pre].append(cur)
            course_in_degrees[cur] += 1
        queue = deque([i for i in range(numCourses) if course_in_degrees[i] == 0])
        result = []

        while queue:
            cur_course = queue.popleft()
            result.append(cur_course)
            related_courses = course_list[cur_course]
            for related_course in related_courses:
                course_in_degrees[related_course] -= 1
                if course_in_degrees[related_course] == 0:
                    queue.append(related_course)

        if len(result) == numCourses:
            return result
        else:
            return []
