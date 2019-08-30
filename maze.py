""" Coordinate

      0 1 2 3 4 5 6 X
0    / \_/ \_/ \_/ \
1    \_/ \_/ \_/ \_/
2    / \_/ \_/ \_/ \
3    \_/ \_/ \_/ \_/
Y



maze repr goal:

 _   _   _   _
/ \_/ \_/  _/ \
\_    / \_/  _/
/ \_/  _  \_  \
\_  \_/ \    _/
/ \_  \_  \_/ \
\_   _  \_   _/
/ \_/ \_/ \_  \


"""

class Cell():
    """ Hexagonal cell """
    def __init__(self, x, y, walls=[0,1,2,3,4,5]):
        """ x,y int
            walls : list of number 0..5
        """
        assert((x+y)%2==0), "Invalide cell coordinate %s, %s" % (x,y)
        self.x = x
        self.y = y
        self.walls = set(walls)

    def __repr__(self):
        return '<%s, %s, %s>' % (self.x, self.y, self.walls)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.walls == other.walls)
    def dir_to(self, other):
        """ return direction from current cell to other cell
            value: 0..5 """
        if self.is_adjacent(other):
            if self.x == other.x:
                return 0 if (self.y > other.y) else 3
            if self.x < other.x:
                return 1 if self.y > other.y else 2
            if self.x > other.x:
                return 5 if self.y > other.y else 4

    def is_adjacent(self, other):
        """ return true if the two cells are adjacent.
            That is, if they can share a wall in comon
        """
        if self.y == other.y:
            return False
        if self.y == other.y + 1:
            return (self.x == other.x + 1) or (self.x == other.x - 1)
        if self.y == other.y - 1:
            return (self.x == other.x + 1) or (self.x == other.x - 1)
        if self.x == other.x:
            return (self.y == other.y + 2) or (self.y == other.y - 2)

    def connect(self, other):
        if self.is_adjacent(other):
            direction = self.dir_to(other)
            try:
                self.walls.remove(direction)
                other.walls.remove((direction+3) % 6)
            except:
                pass

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
        repr = "<maze>\n"
        for c in self.cells:
            repr += '%s\n' % c
        return repr

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
    maze = Maze(3,3)
    print(maze)
