"""advent of code day 1.

http://adventofcode.com/2016/day/1
--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting
Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you
visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
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
        # If facing tracker is > compass length, circle back to beginning of
        #   list
        if facing >= len(compass):
            facing = facing - len(compass)
        # Always set facing to the positive-valued index of the list
        #   this prevents issues regarding facing being < -len(compass)
        facing = compass.index(compass[facing])
        return facing
    except Exception, exc:
        print exc


def move(direction, compass, facing, last_point):
    """Move around and return new last_point position."""
    try:
        spaces = int(direction[1:])
        # Track total longitude and latitude from start point
        if compass[facing] == "n":
            last_point[1] += spaces
        elif compass[facing] == "s":
            last_point[1] -= spaces
        elif compass[facing] == "e":
            last_point[0] += spaces
        elif compass[facing] == "w":
            last_point[0] -= spaces
        return last_point
    except Exception, exc:
        print exc


def crosscheck(lat, check_line, past_lines):
    """Check if current line crosses past_lines."""
    try:
        sort_check_line = sorted(check_line)
        # print "check line:", sort_check_line
        if lat:
            # line is horizontal
            # check current line against all past lines, except most-recent
            # past line.
            for past_line in past_lines[:-1]:
                sort_past_line = sorted(past_line)
                # print "past line:", sort_past_line
                in_lat = (sort_check_line[0][0] <= sort_past_line[0][0]
                          and sort_check_line[1][0] >= sort_past_line[1][0])
                in_lon = (sort_check_line[0][1] >= sort_past_line[0][1]
                          and sort_check_line[1][1] <= sort_past_line[1][1])
                if in_lat and in_lon:
                    printout(sort_past_line[0][0], sort_check_line[0][1])
        else:
            # line is vertical
            # check current line against all past lines, except most-recent
            # past line.
            for past_line in past_lines[:-1]:
                sort_past_line = sorted(past_line)
                # print "past line:", sort_past_line
                in_lat = (sort_check_line[0][0] >= sort_past_line[0][0]
                          and sort_check_line[1][0] <= sort_past_line[1][0])
                in_lon = (sort_check_line[0][1] <= sort_past_line[0][1]
                          and sort_check_line[1][1] >= sort_past_line[1][1])
                if in_lat and in_lon:
                    printout(sort_check_line[0][0], sort_past_line[0][1])

    except Exception, exc:
        print exc


def printout(lat, lon):
    """Print distance from 0,0 and exit."""
    total = abs(lat) + abs(lon)
    print total
    sys.exit()


if __name__ == "__main__":
    indir = []
    with open(sys.argv[1]) as f:
        for elem in string.split(f.read()):
            indir.append(string.rstrip(elem, ","))

    compass = ["n", "e", "s", "w"]
    facing = 0
    lat = 0
    lon = 0
    # lat is +E -W
    # lon is +N  -S
    visited_coords = [[0, 0]]
    vert_lines = []
    hor_lines = []

    for direction in indir:
        facing = face(direction, compass, facing)
        [lat, lon] = visited_coords[-1]
        new_point = move(direction, compass, facing, [lat, lon])
        if compass[facing] == "n" or compass[facing] == "s":
            crosscheck(False, [visited_coords[-1], new_point], hor_lines)
            vert_lines.append([visited_coords[-1], new_point])
        else:
            crosscheck(True, [visited_coords[-1], new_point], vert_lines)
            hor_lines.append([visited_coords[-1], new_point])
        visited_coords.append(new_point)

    printout(visited_coords[-1][0], visited_coords[-1][1])
