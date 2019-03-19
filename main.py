import turtle
from maze import Maze
from mouse import Mouse
from tree import Tree

wn = turtle.Screen()
wn.bgcolor('lightgray')

michelangelo = turtle.Turtle()

vertical = [
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 3, 1, 1],
]
horizontal = [
    [1, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
]

my_maze = Maze(michelangelo, vertical, horizontal)
my_maze.prepare_turtle(5, 'orange', 'turtle')
my_maze.set_start((30, 230))
my_maze.draw()
my_maze.wait_donatelo()

don = turtle.Turtle()
donatelo = Mouse(don, my_maze)
donatelo.prepare_turtle(3, 'purple', 'turtle', 1)
donatelo.set_start((-135, 185))

sprinter = Tree((0, 0))
sprinter.update_tree(donatelo.positions_options)
sprinter.find_exit()

directions = sprinter.trace_route()
directions.reverse()

donatelo.walk_to_exit(directions)




wn.mainloop()
