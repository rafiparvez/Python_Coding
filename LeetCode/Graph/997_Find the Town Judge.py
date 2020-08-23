class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        indegree = dict()
        outdegree = dict()

        for a, b in trust:
            indegree[b] = indegree.get(b, 0) + 1
            outdegree[a] = outdegree.get(a, 0) + 1

        for person in range(1, N + 1):
            if indegree.get(person, 0) == N - 1 and outdegree.get(person,
                                                                  0) == 0:
                return person
        return -1
