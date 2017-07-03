"""--- Day 10: Balance Bots ---

You come upon a factory in which many robots are zooming around handing small microchips to each other.

Upon closer examination, you notice that each bot only proceeds when it has two microchips, and once it does, it gives each one to a different bot or puts it in a marked "output" bin. Sometimes, bots take microchips from "input" bins, too.

Inspecting one of the microchips, it seems like they each contain a single number; the bots must use some logic to decide what to do with each chip. You access the local control computer and download the bots' instructions (your puzzle input).

Some of the instructions specify that a specific-valued microchip should be given to a specific bot; the rest of the instructions indicate what a given bot should do with its lower-value or higher-value chip.

For example, consider the following instructions:

value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 chip and a value-5 chip.
Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its higher one (5) to bot 0.
Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in output 0.
In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a value-2 microchip, and output bin 2 contains a value-3 microchip. In this configuration, bot number 2 is responsible for comparing value-5 microchips with value-2 microchips.

Based on your instructions, what is the number of the bot that is responsible for comparing value-61 microchips with value-17 microchips?
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
