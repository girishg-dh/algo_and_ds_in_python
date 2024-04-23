from collections import deque

def can_finish(nCourses, prerequisites):
    if nCourses == 0:
        return True
    inDegree = {i:0 for i in range(nCourses)}
    graph = {i : [] for i in range(nCourses)}

    for edge in prerequisites:
        parent, child = edge[0], edge[1]
        inDegree[child] +=  1
        graph[parent].append(child)

    start_course = deque()
    for k in inDegree:
        if inDegree[k] == 0:
            start_course.append(k)
    finished_courses = 0
    while start_course:
        started_course = start_course.popleft()
        for child in graph[started_course]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                start_course.append(child)
        finished_courses += 1

    return finished_courses == nCourses