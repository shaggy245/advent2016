"""2016 advent of code day 2.

You finally arrive at the bathroom (it's a several minute walk from the lobby
so visitors can behold the many fancy conference rooms and water coolers on
this floor) and go to punch in the code. Much to your bladder's dismay, the
keypad is not at all like you imagined it. Instead, you are confronted with
the result of hundreds of man-hours of bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D

You still start at "5" and stop when you're at an edge, but given the same
instructions as above, the outcome is very different:

You start at "5" and don't move at all (up and left are both edges), ending
at 5.
Continuing from "5", you move right twice and down three times (through "6",
"7", "B", "D", "D"), ending at D.
Then, from "D", you move five more times (through "D", "B", "C", "C", "B"),
ending at B.
Finally, after five more moves, you end at 3.
So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is the correct bathroom
code?
"""

import string
import sys


def move(movements, cur):
    """Move around the keypad."""
    new_loc = cur[:]
    for direction in movements:
        dir_index = dirs[direction][0]
        dir_impact = dirs[direction][1]
        new_loc[dir_index] = cur[dir_index] + dir_impact
        if new_loc[dir_index] < 0:
            new_loc[dir_index] = 0
        elif new_loc[dir_index] > 4:
            new_loc[dir_index] = 4
        if keypad[new_loc[0]][new_loc[1]] == "*":
            new_loc = cur[:]
        else:
            cur = new_loc[:]
    return cur


with open(sys.argv[1]) as f:
    indir = f.read().split("\n")

keypad = (("*", "*", "1", "*", "*"), ("*", "2", "3", "4", "*"),
          ("5", "6", "7", "8", "9"), ("*", "A", "B", "C", "*"),
          ("*", "*", "D", "*", "*"))

# Use dirs to track available keypad directions and their impact on movement
#   through the keypad hash
dirs = {"U": [0, -1], "D": [0, 1], "L": [1, -1], "R": [1, 1]}
keyseq = []
cur_loc = [2, 0]

for keydir in indir:
    if len(keydir) > 0:
        # print(cur_loc)
        cur_loc = move(keydir.strip(), cur_loc)
        keyseq.append(keypad[cur_loc[0]][cur_loc[1]])

print("".join(keyseq))
