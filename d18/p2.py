#!/usr/bin/env python3

from bisect import bisect_left
from sys import stdin
from typing import Generator

SIZE = 70


def neighbors_of(point: tuple[int, int]) -> Generator:
    for k in range(4):
        neigh = list(point)
        neigh[k % 2] += (-1) ** (k // 2)

        if neigh[k % 2] < 0 or neigh[k % 2] > SIZE:
            continue
        yield neigh[0], neigh[1]


def dfs(bad_points: set[tuple[int, int]]) -> bool:
    start = 0, 0
    visited = set()
    q = [start]

    while q:
        point = q.pop()
        if point in visited:
            continue
        if point == (SIZE, SIZE):
            return True
        visited.add(point)

        for neigh in neighbors_of(point):
            if neigh in bad_points:
                continue
            q.append(neigh)
    return False


if __name__ == "__main__":
    bad_points = []
    for line in stdin:
        fields = line.strip().split(",")
        bad_points.append((int(fields[0]), int(fields[1])))

    def check_for(i: int) -> bool:
        return not dfs(set(bad_points[:(i+1)]))

    ans = bisect_left(range(len(bad_points)), True, key=check_for)
    print(f"{bad_points[ans][0]},{bad_points[ans][1]}")
