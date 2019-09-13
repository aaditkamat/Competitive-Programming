# Title: Number of Islands
# Runtime: 292 ms
# Memory: 14.7 MB

Point = collections.namedtuple("Point", ['x', 'y'])


class Solution:
    # Time Complexity: O(size) where size refers to the size of the grid
    # Space Complexity: O(size) to store the visited state for each cell in the grid
    def setUpVisited(self, grid: List[List[str]]) -> List[List[bool]]:
        is_visited = []
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[i])):
                row.append(False)
            is_visited.append(row)
        return is_visited

    def BFS(self, grid: List[List[str]], x: int, y: int,
            is_visited: List[List[bool]]):
        queue = [Point(x, y)]
        while queue:
            curr = queue.pop(0)
            if curr.x in range(len(grid)) and curr.y in range(len(
                    grid[0])) and grid[curr.x][
                        curr.y] == '1' and not is_visited[curr.x][curr.y]:
                is_visited[curr.x][curr.y] = True
                queue.extend([
                    Point(curr.x - 1, curr.y),
                    Point(curr.x + 1, curr.y),
                    Point(curr.x, curr.y - 1),
                    Point(curr.x, curr.y + 1)
                ])

    def numIslands(self, grid: List[List[str]]) -> int:
        is_visited = self.setUpVisited(grid)
        num_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and not is_visited[i][j]:
                    self.BFS(grid, i, j, is_visited)
                    num_of_islands += 1
        return num_of_islands