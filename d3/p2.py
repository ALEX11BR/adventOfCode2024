#!/usr/bin/env python3

import re
from sys import stdin

if __name__ == "__main__":
    text = stdin.read().splitlines()

    ans = 0
    disabled = False

    for line in text:
        for match in re.finditer(r"do\(\)|don't\(\)|mul\(([0-9]*),([0-9]*)\)", line):
            if match[0] == "do()":
                disabled = False
            elif match[0] == "don't()":
                disabled = True
            else:
                if not disabled:
                    ans += int(match[1]) * int(match[2])

    print(ans)
