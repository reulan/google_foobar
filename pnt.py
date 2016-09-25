class Point(object):
    """Creates a point class matching a coordinate and including prisoner_id."""

    def __init__(self):
        """Default constructor if point is given no values."""
        self.x = 0
        self.y = 0
        self.pid = 0

    def __init__(self, x, y):
        """Default constructor if point is given values."""
        self.x = x
        self.y = y
        self.pid = 0

    def __str__(self):
        """Prints string representation of point."""
        return ('({sx}, {sy})'.format(sx=self.x, sy=self.y))

    def change_pid(self, pid):
        if 1 <= pid <= 100000:
            self.pid = pid

    def get_pid(self):
        return str(self.pid)

p1 = Point(3, 2)
p1.change_pid(9)
p2 = Point(5, 10)
p2.change_pid(1000000)
p3 = Point(1, 1)
p2.change_pid(-1)
point_list = [p1, p2, p3]

for p in point_list:
    print('Point: {po}\nx: {px}\ny: {py}\npid: {ppid}\n'.format(po=p, px=p.x, py=p.y, ppid=p.pid))
    print(type(p.get_pid()), p.get_pid())
