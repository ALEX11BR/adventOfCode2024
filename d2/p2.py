#!/usr/bin/env python3

from copy import copy
from sys import stdin

if __name__ == "__main__":
    text = stdin.read().splitlines()

    nums = [[int(f) for f in line.split()] for line in text]

    ans = 0
    for report in nums:
        for k in range(len(report)):
            rep = copy(report)
            rep.pop(k)

            ascending = rep[0] < rep[1]
            good = True
            for i in range(1, len(rep)):
                if rep[i] == rep[i - 1] or (rep[i - 1] < rep[i]) != ascending or abs(rep[i - 1] - rep[i]) > 3:
                    good = False
                    break
            if good:
                ans += 1
                break

    print(ans)
