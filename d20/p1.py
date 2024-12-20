#!/usr/bin/env python3

from sys import stdin
from typing import Generator

if __name__ == "__main__":
    text = stdin.read().splitlines()

    def neighbors_of(point: tuple[int, int]) -> Generator[tuple[int, int], None, None]:
        for k in range(4):
            neigh = list(point)
            neigh[k % 2] += (-1) ** (k // 2)

            if text[neigh[0]][neigh[1]] == "#":
                continue
            yield neigh[0], neigh[1]

    def dfs(start: tuple[int, int]) -> dict[tuple[int, int], int]:
        q = [(start, 0)]
        dists = {}

        while q:
            elem, dist = q.pop()
            if elem in dists:
                continue
            dists[elem] = dist

            for neigh in neighbors_of(elem):
                q.append((neigh, dist + 1))
        return dists

    for i in range(1, len(text) - 1):
        for j in range(1, len(text[0]) - 1):
            if text[i][j] == "S":
                start = i, j
            if text[i][j] == "E":
                end = i, j

    ans = 0
    dists = dfs(start)

    for i in range(1, len(text) - 1):
        for j in range(1, len(text[0]) - 1):
            if text[i][j] == "#":
                if (i - 1, j) in dists and (i + 1, j) in dists:
                    economy = max(dists[i - 1, j], dists[i + 1, j]) - \
                        min(dists[i - 1, j], dists[i + 1, j]) - 2
                    if economy >= 100:
                        ans += 1
                if (i, j - 1) in dists and (i, j + 1) in dists:
                    economy = max(dists[i, j - 1], dists[i, j + 1]) - \
                        min(dists[i, j - 1], dists[i, j + 1]) - 2
                    if economy >= 100:
                        ans += 1

    print(ans)
