"""
--- Day 7: Internet Protocol Version 7 ---

While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:

abba[mnop]qrst supports TLS (abba outside square brackets).
abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
How many IPs in your puzzle input support TLS?
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
