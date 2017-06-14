"""
--- Day 8: Two-Factor Authentication ---

You come across a door implementing what you can only assume is an
implementation of two-factor authentication after a long game of requirements
telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a
nearby desk). Then, it displays a code on a little screen, and you type that
code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken
everything apart and figured out how it works. Now you just have to work out
what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for
the screen; these instructions are your puzzle input. The screen is 50 pixels
wide and 6 pixels tall, all of which start off, and is capable of three
somewhat peculiar operations:

rect AxB turns on all of the pixels in a rectangle at the top-left of the
screen which is A wide and B tall.
rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right
by B pixels. Pixels that would fall off the right end appear at the left end of
the row.
rotate column x=A by B shifts all of the pixels in column A (0 is the left
column) down by B pixels. Pixels that would fall off the bottom appear at the
top of the column.
For example, here is a simple sequence on a smaller screen:

rect 3x2 creates a small rectangle in the top-left corner:

###....
###....
.......
rotate column x=1 by 1 rotates the second column down by one pixel:

#.#....
###....
.#.....
rotate row y=0 by 4 rotates the top row right by four pixels:

....#.#
###....
.#.....
rotate column x=1 by 1 again rotates the second column down by one pixel,
causing the bottom pixel to wrap back to the top:

.#..#.#
#.#....
.#.....
As you can see, this display technology is extremely powerful, and will soon
dominate the tiny-code-displaying-screen market. That's what the advertisement
on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display:
after you swipe your card, if the screen did work, how many pixels should be
lit?
"""
import argparse

class Screen(object):

    def __init__(self, width, height):
        self.grid = [["." for x in range(width)] for y in range(height)]

    def enable_pixels(self, width, height):
        for i in range(height):
            for j in range(width):
                self.grid[i][j] = "#"

    def rotate_pixels(self, xy, location, moves):
        orig_grid = [row[:] for row in self.grid]
        if xy == "x":
            less_moves = moves % len(self.grid)
            for i in range(len(self.grid)):
                self.grid[i][location] = orig_grid[i - less_moves][location]
        elif xy == "y":
            less_moves = moves % len(self.grid[location])
            for i in range(len(self.grid[location])):
                self.grid[location][i] = orig_grid[location][i - less_moves]


def parse_input(line, screen):
    if line.startswith("rect "):
        width, height = line.split()[1].split("x")
        screen.enable_pixels(int(width), int(height))
    elif line.startswith("rotate column x="):
        location, moves = line.split("=")[1].split(" by ")
        screen.rotate_pixels("x", int(location), int(moves))
    elif line.startswith("rotate row y="):
        location, moves = line.split("=")[1].split(" by ")
        screen.rotate_pixels("y", int(location), int(moves))


parser = argparse.ArgumentParser(description='Advent of code.')
parser.add_argument('-s','--screendimensions',
                    help="screen dimensions entered as XxY (ex. 3x50)",
                    default="50x6")
parser.add_argument('inputfile', type=argparse.FileType('r'),
                    help='Path to input file')
args = parser.parse_args()
lines = args.inputfile.read().rstrip("\n").split("\n")
width, height = args.screendimensions.split("x")

screen = Screen(int(width), int(height))

for line in lines:
    parse_input(line, screen)

print("".join(["".join(row) for row in screen.grid]).count("#"))
