"""
--- Part Two ---

As the door slides open, you are presented with a second door that uses a slightly more inspired security mechanism. Clearly unimpressed by the last version (in what movie is the password decrypted in order?!), the Easter Bunny engineers have worked out a better solution.

Instead of simply filling in the password from left to right, the hash now also indicates the position within the password to fill. You still look for hashes that begin with five zeroes; however, now, the sixth character represents the position (0-7), and the seventh character is the character to put in that position.

A hash result of 000001f means that f is the second character in the password. Use only the first result for each position, and ignore invalid positions.

For example, if the Door ID is abc:

The first interesting hash is from abc3231929, which produces 0000015...; so, 5 goes in position 1: _5______.
In the previous method, 5017308 produced an interesting hash; however, it is ignored, because it specifies an invalid position (8).
The second interesting hash is at index 5357525, which produces 000004e...; so, e goes in position 4: _5__e___.
You almost choke on your popcorn as the final character falls into place, producing the password 05ace8e3.

Given the actual Door ID and this new method, what is the password? Be extra proud of your solution if it uses a cinematic "decrypting" animation.

Your puzzle input is still wtnhxymk.
"""
import argparse
import hashlib

def md5sum(decoded_string):
    md5 = hashlib.new("md5")
    md5.update(decoded_string.encode("utf-8"))
    return md5.hexdigest()


def calc_password(door_id):
    password = ["_"] * 8
    extra_char = 0
    print("".join(password), end = "\r")
    while "_" in password:
        door_id_md5 = md5sum((door_id + str(extra_char)))
        try:
            if door_id_md5.startswith("00000") and password[int(door_id_md5[5])] == "_":
                password[int(door_id_md5[5])] = door_id_md5[6]
        except Exception:
            pass
        print("".join(password), end="\r")
        extra_char += 1
    return "".join(password)


parser = argparse.ArgumentParser(description='Advent of code.')
parser.add_argument('inputfile', type=argparse.FileType('r'), help='Path to input file')
args = parser.parse_args()
lines = args.inputfile.read().rstrip("\n").split("\n")
door_id = lines[0]

print(calc_password(door_id))
