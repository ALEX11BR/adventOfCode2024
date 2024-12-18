#!/usr/bin/env python3

from collections import deque
from sys import stdin
from typing import Generator

SIZE = 70
FIRST_ELEMS = 1024


def neighbors_of(point: tuple[int, int]) -> Generator:
    for k in range(4):
        neigh = list(point)
        neigh[k % 2] += (-1) ** (k // 2)

        if neigh[k % 2] < 0 or neigh[k % 2] > SIZE:
            continue
        yield neigh[0], neigh[1]


if __name__ == "__main__":
    bad_points = {tuple([int(num) for num in line.split(",")])
                  for line in stdin.read().splitlines()[:FIRST_ELEMS]}

    ans = 0
    start = 0, 0
    visited = set()
    q = deque([(start, 0)])

    while q:
        point, dist = q.popleft()
        if point in visited:
            continue
        if point == (SIZE, SIZE):
            ans = dist
            break
        visited.add(point)

        for neigh in neighbors_of(point):
            if neigh in bad_points:
                continue
            q.append((neigh, dist + 1))

    print(ans)
