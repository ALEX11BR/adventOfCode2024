#!/usr/bin/env python3

from sys import stdin
from typing import Generator

if __name__ == "__main__":
    text = stdin.read().splitlines()

    ans = 0
    filled = set()

    def neighbors_of(point: tuple[int, int], correct: bool = True) -> Generator[tuple[int, int], None, None]:
        for k in range(4):
            new_point = list(point)
            new_point[k // 2] += (-1) ** (k % 2)

            if correct:
                if new_point[k // 2] < 0 or new_point[0] >= len(text) or new_point[1] >= len(text[0]):
                    continue
                if text[new_point[0]][new_point[1]] != text[point[0]][point[1]]:
                    continue

            yield (new_point[0], new_point[1])

    for i in range(len(text)):
        for j in range(len(text[0])):
            if (i, j) in filled:
                continue

            area = 0
            perimeter = 0
            current_points = set()

            q = [(i, j)]
            while q:
                elem = q.pop()
                if elem in filled:
                    continue
                filled.add(elem)
                current_points.add(elem)

                area += 1
                for neigh in neighbors_of(elem, False):
                    if neigh not in current_points:
                        perimeter += 1
                    else:
                        perimeter -= 1

                for neigh in neighbors_of(elem):
                    q.append(neigh)

            ans += area * perimeter

    print(ans)
