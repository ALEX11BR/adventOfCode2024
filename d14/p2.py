#!/usr/bin/env python3

# NOTE: takes about 5 seconds

import re
from sys import stdin
from typing import Generator

WIDTH = 101
HEIGHT = 103
LIMITS = [WIDTH, HEIGHT]

SIZE_THRESH = 100

if __name__ == "__main__":
    data = []
    for line in stdin:
        line = line.strip()

        data.append([int(num) for num in re.findall("[-+0-9]+", line)])

    def neighbors(point: tuple[int, int]) -> Generator[tuple[int, int], None, None]:
        for k in range(4):
            p = list(point)
            p[k % 2] = (p[k % 2] + (-1) ** (k // 2)) % LIMITS[k % 2]

            yield (p[0], p[1])

    ans = 0
    not_found = True
    while not_found:
        locs = set()
        for robot in data:
            coords = [(robot[i] + ans * robot[i + 2]) % LIMITS[i]
                      for i in range(2)]
            locs.add((coords[0], coords[1]))

        while len(locs) >= SIZE_THRESH:
            compo = set()
            loc = locs.pop()
            q = [loc]

            while q:
                loc = q.pop()
                compo.add(loc)

                for neigh in neighbors(loc):
                    if neigh in locs:
                        q.append(neigh)
                        locs.remove(neigh)

            if len(compo) > SIZE_THRESH:
                """
                deb = [[" "] * WIDTH for _ in range(HEIGHT)]
                for j, i in compo:
                    deb[i][j] = "#"
                for i in range(HEIGHT):
                    for j in range(WIDTH):
                        print(deb[i][j], end="")
                    print()
                """
                not_found = False
                break
        if not_found:
            ans += 1

    print(ans)
