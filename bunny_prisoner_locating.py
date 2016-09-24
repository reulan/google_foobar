#/usr/bin/python env
#bunny_prisoner_locating.py
#mpmsimo
#9/23/16

import sys
import math

def answer(x, y):
    """Dynamically create a matrix at will until bunny is identified."""
    # Create counters for use with maths!
    min_num = 1
    max_num = 100000
    lc = 0 # Count amount of lists
    prisoner_count = 1

    print('Searching for bunny in cell ({xn},{yn}).'.format(xn=x, yn=y))

    matrix = [] # Will add additional lists later

    # Dynamically label bunnies with ID's (Always add new Y-axis list)
    if not matrix:
        matrix.append([prisoner_count])
        prisoner_count += 1
        lc += 1
        print('Bunny #{n} has been jailed in ({xi},{yi})'.format(n=prisoner_count, xi=lc, yi=min_num))

    # Add a new list to matrix (represents y-axis)
    for e in xrange(0, max_num):
        matrix.append([prisoner_count])
        prisoner_count += 1
        lc += 1
        print('Bunny #{n} has been jailed in ({xi},{yi})'.format(n=prisoner_count, xi=lc, yi=e+1))

        # For each existing list, append a value (represents x-axis)
        for l in xrange(0, lc):
            matrix[l].append(prisoner_count)
            prisoner_count += 1
            print('Bunny #{n} has been jailed in ({xi},{yi})'.format(n=prisoner_count, xi=lc, yi=e+1))
        try:
            prisoner_id = str(matrix[x-1][y-1])
            #print('Bunny #{n} has been jailed'.format(n=prisoner_count))
            print('Bunny in cell ({xn},{yn}) has ID {pid}.\n'.format(xn=x, yn=y, pid=prisoner_id))
            return prisoner_id
        except IndexError as ie:
            continue

if __name__ == '__main__':
    answer(1, 1)
    answer(2, 1)
    answer(1, 2)
    answer(3, 2)
    answer(5, 10)
    #answer(10,10)
    #answer(100,100)
