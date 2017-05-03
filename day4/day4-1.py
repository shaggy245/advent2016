"""
--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course,
the list is encrypted and full of decoy data, but the instructions to decode
the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes)
followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in
the encrypted name, in order, with ties broken by alphabetization. For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a
(5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all
tied (1 of each), the first five are listed alphabetically.
not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.
Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?
"""
import sys
import re


def find_legit(room):
    room_char_count = []
    for char in sorted(set("".join(room[0:-2]))):
        room_char_count.append((char,"".join(room[0:-2]).count(char)))
    # sort by count and return
    checksum = "".join([i[0] for i in sorted(room_char_count, key=lambda char: char[1], reverse=True)[0:5]])
    if checksum == room[-1]:
        return int(room[-2])
    else:
        return 0

with open(sys.argv[1]) as f:
    lines = f.read().rstrip("\n").split("\n")

sector_sum = 0

for line in lines:
    room_datum = re.split("-|\[", line.rstrip("]"))
    sector_sum += find_legit(room_datum)

print(sector_sum)
