"""--- Day 10: Balance Bots ---
day10 - see difference between parsing input list multiple times
"""
import argparse


class Bot(object):

    def __init__(self, botid):
        self.bid = botid
        self.chips = []
        self.compared = []

    def __handoff__(self):
        self.compared.append(tuple(self.chips))
        self.low.addchip(self.chips[0])
        self.high.addchip(self.chips[1])

    def setlowhigh(self, lowdest, highdest):
        self.low = lowdest
        self.high = highdest

    def addchip(self, chip):
        self.chips.append(int(chip))
        if len(self.chips) > 1:
            self.chips.sort()
            self.__handoff__()


class Bin(object):

    def __init__(self, binid):
        self.bid = binid
        self.chips = []


    def addchip(self, chip):
        self.chips.append(chip)


def add_highlow(btype, bid):
    global bots
    global bins
    # Check if object is already created, and create if needed
    if btype == "bot" and bid not in bots:
        newobj = Bot(bid)
        bots[bid] = newobj
    elif btype == "bot":
        newobj = bots[bid]
    elif btype == "output" and bid not in bins:
        newobj = Bin(bid)
        bins[bid] = newobj
    elif btype == "output":
        newobj = bins[bid]

    return newobj


parser = argparse.ArgumentParser(description='Advent of code.')
parser.add_argument('inputfile', type=argparse.FileType('r'), help='Path to input file')
args = parser.parse_args()
lines = args.inputfile.read().rstrip("\n").split("\n")

slines = sorted(lines)

# Build dicts in which to store bins and bots
bots = {}
bins = {}

# Build bot and bin objects into bots and bins dicts
for sline in slines:
    words = sline.split()
    if words[0] == "bot":
        lowobj = add_highlow(words[5], words[6])
        highobj = add_highlow(words[10], words[11])

        if words[1] not in bots:
            bots[words[1]] = Bot(words[1])
            bots[words[1]].setlowhigh(lowobj, highobj)
        elif words[1] in bots:
            bots[words[1]].setlowhigh(lowobj, highobj)

    else:
        # parse the "value" lines
        bots[words[-1]].addchip(words[1])


for bid, bot in bots.items():
    if tuple(sorted([61, 17])) in bot.compared:
        print(bid, bot.compared)
