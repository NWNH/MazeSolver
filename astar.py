import heapq


def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def astar(maze, start, end):

    rows = len(maze)
    cols = len(maze[0])

    open_set = []

    heapq.heappush(open_set, (0, start))

    parent = {}

    g_score = {}

    g_score[start] = 0


    visited = set()

    search_order = []


    while open_set:

        _, current = heapq.heappop(open_set)


        if current in visited:
            continue


        visited.add(current)

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
            ):


                neighbor = (nx, ny)


                tentative_g = g_score[current] + 1


                if neighbor not in g_score or tentative_g < g_score[neighbor]:


                    g_score[neighbor] = tentative_g


                    f = tentative_g + heuristic(neighbor, end)


                    heapq.heappush(
                        open_set,
                        (f, neighbor)
                    )


                    parent[neighbor] = current



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

    m = Maze(21,21)

    grid = m.generate()


    start = (1,1)

    end = (19,19)


    path, visited = astar(
        grid,
        start,
        end
    )


    print("路径长度:",len(path))

    print("搜索节点数:",len(visited))
