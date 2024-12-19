#!/usr/bin/env python3

# NOTE: takes about 24 seconds

import re
from sys import stdin

if __name__ == "__main__":
    patterns = input().split(", ")
    input()

    towels = [line.strip() for line in stdin]

    i = 0
    while i < len(patterns):
        j = 0
        while j < len(patterns):
            pattern = patterns[j]
            if patterns[i].startswith(pattern) and patterns[i][len(pattern):] in patterns:
                patterns.pop(i)
                i -= 1
                break
            j += 1
        i += 1

    re_str = f"^(?:(?:{patterns[0]})"
    for pattern in patterns[1:]:
        re_str += f"|(?:{pattern})"
    re_str += ")+$"

    re_match = re.compile(re_str)

    ans = len(list(filter(lambda s: re_match.match(s), towels)))

    print(ans)
