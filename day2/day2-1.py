"""2016 advent of code day 2.

The document goes on to explain that each button to be pressed can be found by
starting on the previous button and moving to adjacent buttons on the keypad:
U moves up, D moves down, L moves left, and R moves right. Each line of
instructions corresponds to one button, starting at the previous button (or,
for the first line, the "5" button); press whatever button you're on at the end
of each line. If a move doesn't lead to a button, ignore it.

You can't hold it much longer, so you decide to figure out the code as you walk
to the bathroom. You picture a keypad like this:

1 2 3
4 5 6
7 8 9
Suppose your instructions are:

ULL
RRDDD
LURDL
UUUUD
You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and
stay on "1"), so the first button is 1.
Starting from the previous button ("1"), you move right twice (to "3") and then
down three times (stopping at "9" after two moves and ignoring the third),
ending up with 9.
Continuing from "9", you move left, up, right, down, and left, ending with 8.
Finally, you move up four times (stopping at "2"), then down once, ending with
5.
So, in this example, the bathroom code is 1985.

Your puzzle input is the instructions from the document you found at the front
desk. What is the bathroom code?
"""

import string
import sys


def move(movements, cur):
    """Move around the keypad."""
    for direction in movements:
        dir_index = dirs[direction][0]
        dir_impact = dirs[direction][1]
        cur[dir_index] += dir_impact
        if cur[dir_index] < 0:
            cur[dir_index] = 0
        elif cur[dir_index] > 2:
            cur[dir_index] = 2
    return cur


with open(sys.argv[1]) as f:
    indir = f.read().split("\n")

keypad = (("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9"))
# Use dirs to track available keypad directions and their impact on movement
#   through the keypad hash
dirs = {"U": [0, -1], "D": [0, 1], "L": [1, -1], "R": [1, 1]}
keyseq = []
cur_loc = [1, 1]

for keydir in indir:
    if len(keydir) > 0:
        # print(cur_loc)
        cur_loc = move(keydir.strip(), cur_loc)
        keyseq.append(keypad[cur_loc[0]][cur_loc[1]])

print("".join(keyseq))
