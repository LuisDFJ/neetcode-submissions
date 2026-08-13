from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        tray = deque(sandwiches)
        while queue:
            l = len(queue)
            for _ in range(l):
                if queue[0] == tray[0]:
                    queue.popleft()
                    tray.popleft()
                else:
                    queue.append(queue.popleft())
            if l == len(queue): break
        return len(queue)
        