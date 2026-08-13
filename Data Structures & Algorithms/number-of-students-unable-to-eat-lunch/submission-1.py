from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sCounter = Counter(students)
        for i,sandwich in enumerate(sandwiches):
            if sCounter[sandwich]:
                sCounter[sandwich] -= 1
            else:
                return len(sandwiches) - i
        return 0

        