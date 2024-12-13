#!/usr/bin/env python3

from math import floor
import re
from sys import stdin

if __name__ == "__main__":
    text = stdin.read().splitlines()

    ans = 0

    for i in range(0, len(text), 4):
        a = re.match("Button A: X\\+([0-9]*), Y\\+([0-9]*)", text[i])
        b = re.match("Button B: X\\+([0-9]*), Y\\+([0-9]*)", text[i + 1])
        p = re.match("Prize: X=([0-9]*), Y=([0-9]*)", text[i + 2])

        assert (a is not None and b is not None and p is not None)

        ax = int(a[1])
        ay = int(a[2])
        bx = int(b[1])
        by = int(b[2])
        px = int(p[1])
        py = int(p[2])

        det = ax * by - ay * bx

        alpha = (px * by - py * bx) / det
        beta = (ax * py - ay * px) / det

        if floor(alpha) != alpha or floor(beta) != beta:
            continue

        ans += int(alpha) * 3 + int(beta)

    print(ans)
