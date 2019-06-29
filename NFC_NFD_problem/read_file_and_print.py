import sys

filename = sys.argv[1]
with open(filename, encoding='utf-8') as f:
    for line in f:
        print(line.strip())
