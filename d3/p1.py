#!/usr/bin/env python3

import re
from sys import stdin

if __name__ == "__main__":
    text = stdin.read().splitlines()

    ans = 0

    for line in text:
        for match in re.finditer(r"mul\(([0-9]*),([0-9]*)\)", line):
            ans += int(match[1]) * int(match[2])

    print(ans)
