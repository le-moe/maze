class Cell():
    """ Hexagonal cell """
    def __init__(self, x, y, walls=[0,1,2,3,4,5]):
        """ x,y int
            walls : list of number 0..5
        """
        assert((x+y)%2==0), "Invalide cell coordinate %s, %s" % (x,y)
        self.x = x
        self.y = y
        self.inside = None
        self.walls = set(walls)
        self.in_maze = False

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

    def __contains__(self, wall):
        # 4 in cell
        return wall in self.walls

    def mark(self, char='X'):
        assert(len(char)==1), "Can only put on char in the cell"
        self.inside = char

    def labeled_walls(self):
        labeled_walls = []
        id = '%s:%s' % (self.x, self.y)
        for w in self.walls:
            label = '%s_%s' % (id,w)
            labeled_walls.append(label)
        return labeled_walls
