"""advent of code day 1.

http://adventofcode.com/2016/day/1
"""

import sys
import string


def face(direction, facing):
    """Keep track of facing direction."""
    try:
        lr = direction[0]
        if lr == "R":
            facing += 1
        elif lr == "L":
            facing -= 1

        facing = facing % 4

        return facing
    except Exception, exc:
        print exc


def move(direction, facing, lat, lon):
    """Move around and return new lat or lon position."""
    try:
        spaces = int(direction[1:])
        # Track total longitude and latitude from start point
        if facing == 0:
            lon += spaces
        elif facing == 2:
            lon -= spaces
        elif facing == 1:
            lat += spaces
        elif facing == 3:
            lat -= spaces
        return lat, lon
    except Exception, exc:
        print exc


if __name__ == "__main__":
    indir = []
    with open(sys.argv[1]) as f:
        indir = string.split(f.read(), ", ")

    facing = 0
    lat = 0
    lon = 0
    # lat is +E -W
    # lon is +N  -S

    for direction in indir:
        direction = direction.strip()
        facing = face(direction, facing)
        lat, lon = move(direction, facing, lat, lon)

    total = abs(lon) + abs(lat)
    print total
