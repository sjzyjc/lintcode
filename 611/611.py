from collections import deque
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        if not grid or not grid[0]:
            return -1

        queue = deque([source])
        distance = 0
        offsets = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
        while queue:
            length = len(queue)
            for i in range(length):
                point = queue.popleft()
            
                if not (0 <= point.x < len(grid) and 0 <= point.y < len(grid[0])):
                    continue
                
                if grid[point.x][point.y] == 1:
                    continue
                
                grid[point.x][point.y] = 1
                if point.x == destination.x and point.y == destination.y:
                    return distance
                    
                for offset in offsets:
                    queue.append(Point(point.x + offset[0], point.y + offset[1]))
                
            distance += 1

        return -1