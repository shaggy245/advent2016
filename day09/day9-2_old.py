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


def grab_number(line):
    track = 0
    numchars = ""
    while line[track] in "0123456789":
         numchars += line[track]
         track += 1
    return int(numchars)


def grab_marker(line):
    track = 0
    marker = ""
    while line[track] in "(0123456789x)":
        marker += line[track]
        if line[track] == ")":
            break
        track += 1
    return marker


def count_sequences(line):
    shorter_line = ""
    temp_count = 0
    i = 0
    while i < len(line):
        if line[i]=="(":
            shorter_line += str(temp_count)
            marker = grab_marker(line[i:])
            i += len(marker)
            shorter_line += marker
            temp_count = 0
        else:
            temp_count += 1
            i += 1
    shorter_line += str(temp_count)
    print(shorter_line)

def strip_chars(line):
    i = 0
    ccount = 0
    while line[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        ccount +=  1
        i += 1
    return ccount


def yikes_rec3(line, ccount):
    i = 0
    ddata = ""
    tempcount = strip_chars(line)
    ccount += tempcount
    ddata = line[tempcount:]
    print("DDATA:",ddata)
    while ddata[i] == "(":
        print(ddata[i:])
        marker = grab_marker(ddata[i:])
        print(marker)
        char_count, dup = [int(y) for y in marker[1:-1].split("x")]
        #decompress += char_count * dup
        ddata += line[(i + len(marker)):(i + len(marker) + char_count)] * dup
        # ddata += line[0:(char_count * dup)]
        #print("DDATA marker ddata: ", ddata, len(ddata))
        #print("DDATA marker line: ", line, len(line))
        i += len(marker)
        print("DDATA marker line: ", line, len(line), ccount)
        print("DDATA marker ddata: ", ddata, len(ddata), ccount)

    if "(" in ddata:
        yikes_rec3(ddata[:], ccount)
    else:
        #print(decompress)
        ccount += len(ddata)
        print("FINAL DDATA: ", len(ddata), ccount)
        return ccount


def yikes_rec2(line, ccount):
    i = 0
    ddata = ""
    tempcount = strip_chars(line)
    ccount += tempcount
    i += tempcount
    ddata = line[i:]
    if line[i] in "(0123456789x)":
        marker = grab_marker(line[i:])
        char_count, dup = [int(y) for y in marker[1:-1].split("x")]
        #decompress += char_count * dup
        ddata = line[(i + len(marker)):(i + len(marker) + char_count)] * dup + line[(i + len(marker) + char_count):]
        # ddata += line[0:(char_count * dup)]
        print("DDATA marker line: ", line, len(line), ccount)
        print("DDATA marker ddata: ", ddata, len(ddata), ccount)
    if "(" in ddata:
        yikes_rec2(ddata[:], ccount)
    else:
        #print(decompress)
        ccount += len(ddata)
        print("FINAL DDATA: ", len(ddata), ccount)
        return ccount


def yikes_rec(line, ccount):
    i = 0
    ddata = ""
    while i < len(line):
        if line[i] in "(0123456789x)":
            marker = grab_marker(line[i:])
            char_count, dup = [int(y) for y in marker[1:-1].split("x")]
            #decompress += char_count * dup
            ddata += line[(i + len(marker)):(i + len(marker) + char_count)] * dup
            # ddata += line[0:(char_count * dup)]
            #print("DDATA marker ddata: ", ddata, len(ddata))
            #print("DDATA marker line: ", line, len(line))
            i += len(marker) + char_count
        else:
            #decompress += 1
            print("a")
            ddata += line[i]
            ccount += 1
            #print("DDATA char ddata: ",ddata, len(ddata))
            #print("DDATA char line: ", line, len(line))
            i += 1
    if "(" in ddata:
        #print("###############################################")
        yikes_rec(ddata[:], ccount)
    else:
        #print(decompress)
        print("FINAL DDATA: ", len(ddata), ccount)
        return len(ddata)


def yikes(line):
    decompress = 0
    i = 0
    while i < len(line):
        if line[i]=="(":
            marker = grab_marker(line[i:])
            char_count, dup = [int(y) for y in marker[1:-1].split("x")]
            decompress += char_count * dup
            i += len(marker) + char_count
        else:
            decompress += 1
            i += 1
    print(decompress)


parser = argparse.ArgumentParser(description='Advent of code.')
parser.add_argument('inputfile', type=argparse.FileType('r'),
                    help='Path to input file')
args = parser.parse_args()
line = args.inputfile.read().rstrip("\n")
print(line)
#count_sequences(line)
print(yikes_rec3(line, 0))
