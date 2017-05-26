import sys

with open(sys.argv[1]) as f:
    lines = f.read().rstrip("\n").split("\n")

print("".join([sorted(([row[i] for row in lines ]), key=([row[i] for row in lines]).count, reverse=True)[0] for i in range(len(lines[0]))]))
