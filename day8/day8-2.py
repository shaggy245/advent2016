"""
--- Part Two ---

You notice that the screen is only capable of displaying capital letters; in
the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?
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

    def print_by_section(self, width, height):
        for i in range(0, len(self.grid[0]), width):
            print("\n")
            for row in self.grid:
                print("".join(row[i:i+width]))

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
width, height = [int(i) for i in args.screendimensions.split("x")]

screen = Screen(width, height)

for line in lines:
    parse_input(line, screen)

screen.print_by_section(5,6)
