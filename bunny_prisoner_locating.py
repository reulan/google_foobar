#/usr/bin/python env
#bunny_prisoner_locating.py
#mpmsimo
#9/24/16
# Time limit exceeded

import time

start_time = time.time()

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

    def change_x(self, x):
        self.x = x

    def change_y(self, y):
        self.y = y

    def change_pid(self, pid):
        if 1 <= pid <= 100000:
            self.pid = pid
        else:
            self.pid = -1

    def get_pid(self):
        return str(self.pid)

def locate_bunny(b, x, y):
    """Attempts to locate a bunny in a cell row."""
    if b.x == y and b.y == x:
        return b.get_pid()
    else:
        return

def verify_possibility(x, y):
    """Verfies if the coordinate given will fall within bounds."""
    # Sorry for the hack google :(
    if x < 1 or x > 319 or y < 1:
        return False
    else:
        return True

def answer(x, y):
    """Given a coordinate, determine prisoner ID range, and give ID."""
    prisoner_count = 1
    bunny_found = False
    cell_row = [] # This will be a list of points that rewrites itself to avoid memory error?

    is_possible = verify_possibility(x, y)
    if not is_possible:
        return

    # Lock up the first bunny
    if len(cell_row) == 0:
        p = Point(1, 1)
        p.change_pid(prisoner_count)
        prisoner_count += 1
        cell_row = [p]

    # Figure out how many points are before this coord, and return int.
    while not bunny_found and is_possible:
        # Search for bunny, and checks if it exists.
        try:
            for bunny in cell_row:
                pid = locate_bunny(bunny, x, y)
                if pid != None:
                    bunny_found = True
                    print('Bunny {bpid} located at ({xi}, {yi})'.format(bpid=pid, xi=bunny.x, yi=bunny.y))
                    return pid
        except Exception as e:
            pass

        # If the cell row has one or follow a pattern
        if len(cell_row) >= 1:
            # Create new cell for bunny, add to beginning of list (at end)
            first_bunny_in_row = Point((cell_row[0].x + 1), 1)
            first_bunny_in_row.change_pid(prisoner_count)
            prisoner_count += 1
            cell_row.insert(0, first_bunny_in_row)
            # Modify remaining list (not element 0)
            for b in cell_row[1:]:
                prev_y = b.y
                b.change_y(int(b.y + 1))
                b.change_pid(prisoner_count)
                prisoner_count += 1

if __name__ == '__main__':
    answer(1000,1000)
    answer(129,319)
    answer(12, 73)
    answer(300, 300)
    answer(200, 200)
    answer(129,319)
    answer(-1, 50)
    answer(-33000, 3344)

    print("--- %s seconds ---" % (time.time() - start_time))
