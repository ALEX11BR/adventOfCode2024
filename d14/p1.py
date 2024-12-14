#!/usr/bin/env python3

from functools import reduce
import re
from sys import stdin

WIDTH = 101
HEIGHT = 103
LIMITS = [WIDTH, HEIGHT]

if __name__ == "__main__":
    data = []
    for line in stdin:
        line = line.strip()

        data.append([int(num) for num in re.findall("[-+0-9]+", line)])

    quads = [0] * 4

    for robot in data:
        coords = [(robot[i] + 100 * robot[i + 2]) % LIMITS[i]
                  for i in range(2)]

        for k in range(4):
            fact1 = (-1) ** (k % 2)
            fact2 = (-1) ** (k // 2)

            if fact1 * coords[0] > fact1 * (WIDTH // 2) and fact2 * coords[1] > fact2 * (HEIGHT // 2):
                quads[k] += 1

    ans = reduce(lambda a, b: a * b, quads)

    print(ans)
