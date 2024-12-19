#!/usr/bin/env python3

# NOTE: takes about 1.5 seconds

from sys import stdin

if __name__ == "__main__":
    patterns = input().split(", ")
    input()

    towels = [line.strip() for line in stdin]

    ans = 0
    for towel in towels:
        dyn = [0] * (len(towel) + 1)
        dyn[0] = 1

        for i in range(len(towel)):
            for p in patterns:
                if len(p) > i + 1:
                    continue
                if towel[:i+1].endswith(p):
                    dyn[i + 1] += dyn[i + 1 - len(p)]
        ans += dyn[len(towel)]

    print(ans)
