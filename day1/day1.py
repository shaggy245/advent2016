"""advent of code day 1.

http://adventofcode.com/2016/day/1
"""

import sys
import string


def face(direction, compass, facing):
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


def move(direction, compass, facing, lat, lon):
    """Move around and return new lat or lon position."""
    try:
        spaces = int(direction[1:])
        # Track total longitude and latitude from start point
        if compass[facing] == "n":
            lon += spaces
        elif compass[facing] == "s":
            lon -= spaces
        elif compass[facing] == "e":
            lat += spaces
        elif compass[facing] == "w":
            lat -= spaces
        return lat, lon
    except Exception, exc:
        print exc


if __name__ == "__main__":
    indir = []
    with open(sys.argv[1]) as f:
        indir = string.split(f.read(), ", ")

    compass = ["n", "e", "s", "w"]
    facing = 0
    lat = 0
    lon = 0
    # lat is +E -W
    # lon is +N  -S

    for direction in indir:
        direction = direction.strip()
        facing = face(direction, compass, facing)
        lat, lon = move(direction, compass, facing, lat, lon)

    total = abs(lon) + abs(lat)
    print total
