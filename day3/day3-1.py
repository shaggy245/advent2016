"""--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways
and office furniture that makes up this part of Easter Bunny HQ. This must be a
graphic design department; the walls are covered in specifications for
triangles.

Or are they?

The design document gives the side lengths of each triangle it describes,
but... 5 10 25? Some of these aren't triangles. You can't help but mark the
impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining
side. For example, the "triangle" given above is impossible, because 5 + 10 is
not larger than 25.

In your puzzle input, how many of the listed triangles are possible?

"""

import sys

with open(sys.argv[1]) as f:
    triangles = f.read().split("\n")

triangles_count = 0
not_triangles = 0

for tri in triangles:
    if len(tri) > 0:
        legs = tri.split()
        print("########################")
        print(float(legs[0]), float(legs[1]), float(legs[2]), "|", float(legs[0]) + float(legs[1]), ">", float(legs[2]))
        if float(legs[0]) + float(legs[1]) > float(legs[2]):
            print("LEGIT")
            triangles_count += 1
        else:
            print("NOT LEGIT")
            not_triangles += 1

print(triangles_count)
print(not_triangles)
