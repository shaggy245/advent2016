"""
--- Part Two ---

You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

For example:

aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
How many IPs in your puzzle input support SSL?
"""

import argparse
import re


def has_palindrome(ip_list):
    try:
        for ip in ip_list:
            for i in range(0, (len(ip) - 3)):
                if ip[i] != ip[i+1] and (ip[i] == ip[i + 3] and ip[i+1] == ip[i + 2]):
                    return True
        return False
    except Exception as exc:
        print(exc)


parser = argparse.ArgumentParser(description='Advent of code.')
parser.add_argument('inputfile', type=argparse.FileType('r'), help='Path to input file')
args = parser.parse_args()
lines = args.inputfile.read().rstrip("\n").split("\n")

tls_count = 0

for line in lines:
    temp = re.split("\[|\]", line)
    if (has_palindrome([temp[i] for i in range(0, len(temp), 2)])
        and not has_palindrome([temp[i] for i in range(1, len(temp), 2)])):
        tls_count += 1
print(tls_count)
