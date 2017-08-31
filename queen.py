from collections import namedtuple


class Point:
    def __init__(self, x, y, state=0):
        self.x = x
        self.y = y
        self.state = 0

    def __repr__(self):
        return str(self.state)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return self.state + other.state

    def place_queen(self):
        self.state = 1


class Board:
    def __init__(self, n):
        self.matrix = Matrix(n)

    def __repr__(self):
        for i in self.matrix:
            print(str(i))

    def is_safe(self, p):
        return (sum((i.state for i in self.matrix.diagonal(p))) +
                sum((i.state for i in self.matrix.column(p.y))) +
                sum((i.state for i in self.matrix.row(p.x)))) < 1

    def solve(self):
        for row in self.matrix:
            for cell in row:
                if self.is_safe(cell):
                    self.matrix[cell.x][cell.y].place_queen()
                    print(sum((i.state for i in self.matrix.diagonal(cell))),
                          sum((i.state for i in self.matrix.column(cell.y))),
                          sum((i.state for i in self.matrix.row(cell.x))))


class Matrix:
    def __init__(self, n):
        self.matrix = [[]] * n
        for i in range(n):
            self.matrix[i] = [Point(r, i) for r in range(n)]
        self.dim = n

    def __getitem__(self, item):
        return self.matrix.__getitem__(item)

    def row(self, i):
        return self.matrix[i]

    def column(self, i):
        return [row[i] for row in self.matrix]

    def diagonal(self, p):
        rp = p.x + p.y
        rm = p.x - p.y
        for row in self.matrix:
            for item in row:
                if item.x - item.y == rm or item.x + item.y == rp:
                    yield item


b = Board(10)
for i in b.matrix:
    print(i)
print ()
b.solve()
for i in b.matrix:
    print(i)