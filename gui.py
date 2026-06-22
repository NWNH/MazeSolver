import tkinter as tk

from maze import Maze
from bfs import bfs
from astar import astar


CELL = 25


class MazeGUI:

    def __init__(self):

        self.window = tk.Tk()

        self.window.title("Maze Solver")


        self.canvas = tk.Canvas(
            self.window,
            width=21*CELL,
            height=21*CELL
        )

        self.canvas.pack()


        frame = tk.Frame(self.window)
        frame.pack()

        self.info = tk.Label(

            self.window,

            text=""

        )

        self.info.pack()


        tk.Button(
            frame,
            text="Generate",
            command=self.generate
        ).pack(side=tk.LEFT)


        tk.Button(
            frame,
            text="BFS",
            command=self.run_bfs
        ).pack(side=tk.LEFT)


        tk.Button(
            frame,
            text="A*",
            command=self.run_astar
        ).pack(side=tk.LEFT)



        self.maze_obj = Maze(21,21)

        self.generate()



        self.window.mainloop()



    def generate(self):

        self.grid = self.maze_obj.generate()


        self.start = (1,1)

        self.end = (19,19)


        self.draw_maze()



    def draw_maze(self):

        self.canvas.delete("all")


        for i in range(21):

            for j in range(21):


                color = "white"


                if self.grid[i][j]==1:
                    color="black"



                if (i,j)==self.start:
                    color="green"



                if (i,j)==self.end:
                    color="red"



                self.canvas.create_rectangle(

                    j*CELL,
                    i*CELL,

                    (j+1)*CELL,
                    (i+1)*CELL,

                    fill=color,

                    outline="gray"

                )



    def animate(self,visited,path):


        for x,y in visited:


            if (x,y)!=self.start and (x,y)!=self.end:


                self.canvas.create_rectangle(

                    y*CELL,
                    x*CELL,

                    (y+1)*CELL,
                    (x+1)*CELL,

                    fill="skyblue",

                    outline="gray"

                )


                self.window.update()

                self.window.after(15)



        for x,y in path:


            if (x,y)!=self.start and (x,y)!=self.end:


                self.canvas.create_rectangle(

                    y*CELL,
                    x*CELL,

                    (y+1)*CELL,
                    (x+1)*CELL,

                    fill="yellow",

                    outline="gray"

                )


                self.window.update()

                self.window.after(30)




    def run_bfs(self):


        self.draw_maze()


        path,visited = bfs(

            self.grid,

            self.start,

            self.end

        )


        self.animate(

            visited,

            path

        )

        self.info.config(

            text=f"BFS visited:{len(visited)}  path:{len(path)}"

        )



    def run_astar(self):



        self.draw_maze()



        path,visited = astar(

            self.grid,

            self.start,

            self.end

        )


        self.animate(

            visited,

            path

        )

        self.info.config(

            text=f"A* visited:{len(visited)}  path:{len(path)}"

        )



MazeGUI()