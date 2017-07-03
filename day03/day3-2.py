"""--- Part Two ---

Now that you've helpfully marked up their design documents, it occurs to you
that triangles are specified in groups of three vertically. Each set of three
numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds
digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
In your puzzle input, and instead reading by columns, how many of the listed
triangles are possible?
"""

import sys


def get_triangles(lines):
    triangles = []
    # Transpose lines matrix
    cols = [[int(row[i]) for row in lines ] for i in range(len(lines[0]))]
    # Separate each column of data into list of triangle-sides
    for index in range(0, len(cols)):
        triangles.extend([cols[index][x:x+3] for x in range(0, len(cols[index]), 3)])
    return triangles


def test_triangles(triangles):
    triangles_count = 0
    for tri in triangles:
        legs = sorted(tri)
        if len(legs) == 3 and (legs[0] + legs[1] > legs[2]):
            triangles_count += 1
    return triangles_count


with open(sys.argv[1]) as f:
    # Create matrix of input file
    lines = [i.split() for i in f.read().rstrip("\n").split("\n")]

print(test_triangles(get_triangles(lines)))
