"""
--- Part Two ---

Apparently, the file actually uses version two of the format.

In version two, the only difference is that markers within decompressed data
are decompressed. This, the documentation explains, provides much more
substantial compression capabilities, allowing many-gigabyte files to be stored
in only a few kilobytes.

For example:

(3x3)XYZ still becomes XYZXYZXYZ, as the decompressed section contains no
markers.
X(8x2)(3x3)ABCY becomes XABCABCABCABCABCABCY, because the decompressed data
from the (8x2) marker is then further decompressed, thus triggering the (3x3)
marker twice for a total of six ABC sequences.
(27x12)(20x12)(13x14)(7x10)(1x12)A decompresses into a string of A repeated
241920 times.
(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN becomes 445 characters
long.
Unfortunately, the computer you brought probably doesn't have enough memory to
actually decompress the file; you'll have to come up with another way to get
its decompressed length.

What is the decompressed length of the file using this improved format?
"""
from __future__ import print_function
import argparse
import re
import string


def grab_marker(line):
    track = 0
    marker = ""
    while line[track] in "(0123456789x)":
        marker += line[track]
        if line[track] == ")":
            break
        track += 1
    return marker


def count_chars(line):
    ccount = 0
    for char in line:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            ccount +=  1
        else:
            return ccount
    return ccount


def yikes(line, multiplier):
    global decompress_count
    i = 0
    while i < len(line):
        #print(i)
        if line[i]=="(":
            #print("MARKER START:",line[i])
            #print("LINE:",line)
            marker = grab_marker(line[i:])
            char_count, dup = [int(y) for y in marker[1:-1].split("x")]
            ddata = line[(i + len(marker)):(i + len(marker) + char_count)]
            new_multiplier = multiplier * dup
            i += len(marker) + char_count
            #print("DDATA:",ddata)
            #print("UPDATE MULTIPLIER:",new_multiplier)
            while ddata[-1] in "(0123456789x)":
                i += 1
                ddata += line[i]
            yikes(ddata, new_multiplier)
        elif line[i] in list(string.ascii_uppercase):
            lead_char_count = count_chars(line[i:])
            #print("CHARS:",line[i:i+lead_char_count],lead_char_count,multiplier)
            decompress_count += (lead_char_count * multiplier)
            i += lead_char_count
        else:
            break


parser = argparse.ArgumentParser(description='Advent of code.')
parser.add_argument('inputfile', type=argparse.FileType('r'),
                    help='Path to input file')
args = parser.parse_args()
line = args.inputfile.read().rstrip("\n")
decompress_count = 0
#count_sequences(line)
yikes(line,1)
print("FINAL:",decompress_count)
