"""
--- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get
moving.

The room names are encrypted by a state-of-the-art shift cipher, which is
nearly unbreakable without the right software. However, the information kiosk
designers at Easter Bunny HQ were not expecting to deal with a master
cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a
number of times equal to the room's sector ID. A becomes B, B becomes C, Z
becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?
"""

import re
import sys
import string


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

"""
def circle_abc():
    while True:
        for letter in alphabet:
            yield letter
"""

def decode(code):
    for x in " ".join(code[:-2]):
        if x in alphabet:
            
    print(" ".join(code[:-2]), str(int(code[-2]) % 26) )


with open(sys.argv[1]) as f:
    lines = f.read().rstrip("\n").split("\n")

alphabet = list(string.ascii_lowercase)
sector_sum = 0

for line in lines:
    room_datum = re.split("-|\[", line.rstrip("]"))
    room_code = find_legit(room_datum)
    if room_code > 0:
        decode(room_datum)
        #print(line)
    sector_sum += room_code

print(sector_sum)
