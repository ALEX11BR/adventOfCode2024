#!/usr/bin/env python3

from sys import stdin

if __name__ == "__main__":
    relations = []
    arrays = []
    for line in stdin:
        line = line.strip()
        if "|" in line:
            relations.append([int(f) for f in line.split("|")])
        elif line:
            arrays.append([int(f) for f in line.split(",")])

    ans = 0

    for arr in arrays:
        valid = True
        for rel in relations:
            if rel[0] in arr and rel[1] in arr and arr.index(rel[0]) > arr.index(rel[1]):
                valid = False
                break

        if valid:
            ans += arr[len(arr) // 2]

    print(ans)
