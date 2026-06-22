import random


class Maze:
    def __init__(self, rows=21, cols=21):
        self.rows = rows if rows % 2 == 1 else rows + 1
        self.cols = cols if cols % 2 == 1 else cols + 1

        self.maze = [[1 for _ in range(self.cols)]
                     for _ in range(self.rows)]

    def generate(self):

        self.maze = [[1 for _ in range(self.cols)]
                     for _ in range(self.rows)]

        self._dfs(1, 1)

        self.maze[1][1] = 0
        self.maze[self.rows - 2][self.cols - 2] = 0

        return self.maze

    def _dfs(self, x, y):

        self.maze[x][y] = 0

        directions = [
            (0, 2),
            (0, -2),
            (2, 0),
            (-2, 0)
        ]

        random.shuffle(directions)

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if (
                    1 <= nx < self.rows - 1
                    and 1 <= ny < self.cols - 1
                    and self.maze[nx][ny] == 1
            ):

                wall_x = x + dx // 2
                wall_y = y + dy // 2

                self.maze[wall_x][wall_y] = 0

                self._dfs(nx, ny)


if __name__ == "__main__":

    maze = Maze(21, 21)

    grid = maze.generate()

    for row in grid:

        line = ""

        for cell in row:

            if cell == 1:
                line += "██"
            else:
                line += "  "

        print(line)