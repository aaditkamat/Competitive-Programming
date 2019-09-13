# Title: Satisfiability of Equality Equations
# Runtime: 60 ms
# Memory: 14 MB

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
class Solution:
    def BFS(self, first:str, second: str, graph: dict) -> bool:
        queue = collections.deque([first])
        visited = {}
        curr = None
        while queue:
            curr = queue.pop()
            if curr == second:
                return True
            if curr in visited:
                continue
            visited[curr] = True
            if curr in graph:
                queue.extend(graph[curr])
            else:
                break
        return False
    
    def storeEdge(self, graph: dict, first: str, second: str):
        if first not in self.graph:
            self.graph[first] = set([second])
        else:
            self.graph[first] = self.graph[first].union([second]) 
        
    def equationsPossible(self, equations: List[str]) -> bool:
        self.graph = {}
        for equation in equations:
            symbol = '=='
            if symbol in equation:
                first, second = equation.split(symbol)
                self.storeEdge(self.graph, first, second)
                self.storeEdge(self.graph, second, first)
                    
        for equation in equations:
            symbol =  '!='
            if symbol in equation:
                first, second = equation.split(symbol)
                if self.BFS(first, second,self.graph):
                    return False
        return True