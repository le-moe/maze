import math
import random
from cell import *

""" Coordinate

      0 1 2 3 4 5 6 X
0    / \_/ \_/ \_/ \_
1    \_/ \_/ \_/ \_/ \
2    / \_/ \_/ \_/ \_/
3    \_/ \_/ \_/ \_/
Y



maze repr goal:

 _   _   _   _
/ \_/ \_/  _/ \_
\_    / \_/  _  \
/ \_/  _  \_  \_/
\_   _/ \    _/ \
/ \_  \_  \_/  _/
\_   _  \_   _  \
  \_/ \_/ \_/ \_/


"""

class Maze():
    """ Maze of hexagonal cell"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for i in range(width):
            for j in range(height):
                if j%2==0:
                    self.cells.append(Cell(i*2,j))
                else:
                    self.cells.append(Cell(i*2+1,j))

    def __repr__(self):
        repr = "<maze %s, %s>\n" % (self.width, self.height)
        repr += self._to_ascii()
        # for c in self.cells:
        #     repr += '%s\n' % c
        return repr

    def _to_ascii(self):
        """ create a win[x][y]
            X : horizontal axis
            Y : vertical axis
        """
        # initialize the window
        win_w = 4*self.width+1
        win_h = 2*(math.ceil(self.height/2))+1+(1-self.height%2)
        win = [[' ' for _ in range(win_h)] for _ in range(win_w)]
        for c in self.cells:
            x = 2*c.x + 1
            y = c.y +1
            if 0 in c:
                win[x][y-1] = '_'
            if 1 in c:
                win[x+1][y] = '\\'
            if 2 in c:
                win[x+1][y+1] = '/'
            if 3 in c:
                win[x][y+1] = '_'
            if 4 in c:
                win[x-1][y+1] = '\\'
            if 5 in c:
                win[x-1][y] = '/'
            if c.inside:
                win[x][y] = c.inside
        s = '--------------\n'
        for y,_ in enumerate(win[0]):
            for x,_ in enumerate(win):
                s+=win[x][y]
            s+='|\n'
        s += '-----------'
        return s

    # def list_of_walls(self, cells):
    #     list_walls = []
    #     for cell in cells:
    #         list_walls.extend(self.walls_of(cell))
    #     return list_walls

    # def walls_of(self, cell):
    #     list_walls = []
    #     id = '%s:%s' % (cell.x, cell.y)
    #         for w in cell.walls:
    #             label = '%s_%s' % (id,w)
    #             list_walls.append(label)
    #     return list_walls
    def cell_at_coord(self, x,y):
        for c in self.cells:
            if (c.x, c.y) == (x,y):
                return c

    def connect(self, c1, c2):
        if c1.is_adjacent(c2):
            direction = c1.dir_to(c2)
            try:
                c1.walls.remove(direction)
                c2.walls.remove((direction+3) % 6)
            except:
                pass

    def neighbour_cell(self, cell, direction):
        """ return the neighbour cell from cell given in arguments by following direction """
        if direction==0:
            x = cell.x
            y = cell.y -2
        elif direction==1:
            x = cell.x +1
            y = cell.y -1
        elif direction==2:
            x = cell.x +1
            y = cell.y +1
        elif direction==3:
            x = cell.x
            y = cell.y +2
        elif direction==4:
            x = cell.x -1
            y = cell.y +1
        elif direction==5:
            x = cell.x -1
            y = cell.y -1
        return self.cell_at_coord(x,y)

    def all_neighbour(self, cell):
        all_neighbour = []
        for d in range(6):
            if self.neighbour_cell(cell, d):
                all_neighbour.append(self.neighbour_cell(cell, d))
        return all_neighbour

    def randomized_kruskal(self):
        """ 1. Create a list of all walls, and create a set for each cell, each containing just that one cell.
            2. For each wall, in some random order:
                    1. If the cells divided by this wall belong to distinct sets:
                        1. Remove the current wall.
                        2. Join the sets of the formerly divided cells.
        """
        pass

    def randomize_prim(self):
        """1. Start with a grid full of walls.
           2. Pick a cell, mark it as part of the maze. Add the walls of the cell to the wall list.
           3. While there are walls in the list:
                1. Pick a random wall from the list. If only one of the two cells that the wall divides is visited, then:
                    1. Make the wall a passage and mark the unvisited cell as part of the maze.
                    2. Add the neighboring walls of the cell to the wall list.
                2. Remove the wall from the list.
        """
        in_maze = []
        wall_list = []
        random.shuffle(self.cells)
        choice = self.cells.pop()
        wall_list.extend(choice.labeled_walls())
        in_maze.append(choice)
        while len(wall_list) > 0:
            wall = random.choice(wall_list)
            # TODO




def test_cell():
    cM = Cell(3, 1, [])
    c0 = Cell(0, 0, [])
    c1 = Cell(2, 0, [])
    c2 = Cell(4, 0, [])
    c3 = Cell(6, 0, [])
    c4 = Cell(1, 1, [])
    c6 = Cell(5, 1, [])
    c7 = Cell(0, 2, [])
    c8 = Cell(2, 2, [])
    c9 = Cell(4, 2, [])
    c10 = Cell(6, 2, [])
    c11 = Cell(3, 3, [])
    c11 = Cell(3,3, [])
    # check symmetry property
    cells = [cM, c0, c1, c2, c3, c4, c6, c7]
    for cell_i in cells:
        for cell_j in cells:
            if(cell_i != cell_j):
                assert((cell_j.is_adjacent(cell_i) == cell_i.is_adjacent(cell_j)))
    # check coherance
    assert(not cM.is_adjacent(c0))
    assert(cM.is_adjacent(c1))
    assert(cM.is_adjacent(c2))
    assert(not cM.is_adjacent(c3))
    assert(not cM.is_adjacent(c4))
    assert(not cM.is_adjacent(c6))
    assert(not cM.is_adjacent(c7))
    assert(cM.is_adjacent(c8))
    assert(cM.is_adjacent(c9))
    assert(not cM.is_adjacent(c10))
    assert(cM.is_adjacent(c11))

    # test cell direction
    assert(cM.dir_to(c2)==1)
    assert(cM.dir_to(c9)==2)
    assert(cM.dir_to(c11)==3)
    assert(cM.dir_to(c8)==4)
    assert(cM.dir_to(c1)==5)


if __name__ == "__main__":
    test_cell()
    maze = Maze(10,10)
    density = 500
    # for i in range(density):
    #     c = random.choice(maze.cells)
    #     neighbours = maze.all_neighbour(c)
    #     maze.connect(c, random.choice(neighbours))
    c = random.choice(maze.cells)
    c.mark()
    print(len(maze.all_neighbour(c)))
    print(maze)
