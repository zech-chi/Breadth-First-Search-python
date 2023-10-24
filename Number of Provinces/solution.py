class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        counter = 0
        for city in range(len(isConnected)):
            if not city in visited:
                counter += 1
                ## bfs
                queue.append(city)
                visited.add(city)
                while queue:
                    cur_city = queue.popleft()
                    for next_city in range(len(isConnected)):
                        if isConnected[cur_city][next_city] == 1 and not next_city in visited:
                            queue.append(next_city)
                            visited.add(next_city)

        
        return counter
