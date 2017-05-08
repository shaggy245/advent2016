"""
--- Day 5: How About a Nice Game of Chess? ---

You are faced with a security door designed by Easter Bunny engineers that seem to have acquired most of their security knowledge by watching hacking movies.

The eight-character password for the door is generated one character at a time by finding the MD5 hash of some Door ID (your puzzle input) and an increasing integer index (starting with 0).

A hash indicates the next character in the password if its hexadecimal representation starts with five zeroes. If it does, the sixth character in the hash is the next character of the password.

For example, if the Door ID is abc:

The first index which produces a hash that starts with five zeroes is 3231929, which we find by hashing abc3231929; the sixth character of the hash, and thus the first character of the password, is 1.
5017308 produces the next interesting hash, which starts with 000008f82..., so the second character of the password is 8.
The third time a hash starts with five zeroes is for abc5278568, discovering the character f.
In this example, after continuing this search a total of eight times, the password is 18f47a30.

Given the actual Door ID, what is the password?
"""
import argparse
import hashlib


def md5sum(decoded_string):
    md5 = hashlib.new("md5")
    md5.update(decoded_string.encode("utf-8"))
    return md5.hexdigest()


def calc_password(door_id):
    password = ""
    extra_char = 0
    while len(password) < 8:
        door_id_md5 = md5sum((door_id + str(extra_char)))
        if door_id_md5.startswith("00000"):
            password += door_id_md5[5]
        extra_char += 1
    return password


parser = argparse.ArgumentParser(description='Advent of code.')
parser.add_argument('inputfile', type=argparse.FileType('r'), help='Path to input file')
args = parser.parse_args()
lines = args.inputfile.read().rstrip("\n").split("\n")
door_id = lines[0]

print(calc_password(door_id))
