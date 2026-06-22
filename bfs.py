from collections import deque


def bfs(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    queue = deque([start])

    visited = set()
    visited.add(start)

    parent = {}

    search_order = []

    while queue:

        current = queue.popleft()

        search_order.append(current)

        if current == end:
            break

        x, y = current

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if (
                    0 <= nx < rows
                    and 0 <= ny < cols
                    and maze[nx][ny] == 0
                    and (nx, ny) not in visited
            ):

                visited.add((nx, ny))

                parent[(nx, ny)] = current

                queue.append((nx, ny))

    path = []

    if end in parent:

        node = end

        while node != start:

            path.append(node)

            node = parent[node]

        path.append(start)

        path.reverse()

    return path, search_order

from maze import Maze


if __name__ == "__main__":

    m = Maze(21, 21)

    grid = m.generate()

    start = (1, 1)

    end = (19, 19)

    path, visited = bfs(grid, start, end)

    print("路径长度：", len(path))
    print("搜索节点数：", len(visited))