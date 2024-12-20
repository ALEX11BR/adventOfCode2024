#!/usr/bin/env python3

# NOTE: takes about 12 seconds

from collections import deque
from sys import stdin
from typing import Generator

MIN_SKIP = 100

if __name__ == "__main__":
    text = stdin.read().splitlines()

    def neighbors_of(point: tuple[int, int], walls: bool = False) -> Generator[tuple[int, int], None, None]:
        for k in range(4):
            neigh = list(point)
            neigh[k % 2] += (-1) ** (k // 2)

            if not walls and text[neigh[0]][neigh[1]] == "#":
                continue
            if walls and (neigh[k % 2] < 1 or neigh[0] >= len(text) - 1 or neigh[1] >= len(text[0]) - 1):
                continue
            yield neigh[0], neigh[1]

    def bfs(start: tuple[int, int], walls: bool = False) -> dict[tuple[int, int], int]:
        q = deque([(start, 0)])
        dists = {}

        while q:
            elem, dist = q.popleft()
            if walls and dist > 20:
                break
            if elem in dists:
                continue
            dists[elem] = dist

            for neigh in neighbors_of(elem, walls):
                q.append((neigh, dist + 1))
        return dists

    non_walls = set()

    for i in range(1, len(text) - 1):
        for j in range(1, len(text[0]) - 1):
            if text[i][j] == "S":
                start = i, j
            if text[i][j] == "E":
                end = i, j
            if text[i][j] != "#":
                non_walls.add((i, j))

    ans = 0
    dists = bfs(start)

    for start_skip in non_walls:
        wall_dists = bfs(start_skip, True)
        for end_skip in wall_dists:
            if text[end_skip[0]][end_skip[1]] == "#":
                continue

            economy = dists[end_skip] - \
                dists[start_skip] - wall_dists[end_skip]
            if economy < MIN_SKIP:
                continue
            ans += 1

    print(ans)
