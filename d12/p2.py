#!/usr/bin/env python3

from sys import stdin
from typing import Generator

type Side = tuple[tuple[float, float], tuple[float, float]]


def get_neighbor_side(a: tuple[int, int], b: tuple[int, int]) -> Side:
    if a[0] == b[0]:
        return ((a[0] - 0.5, (a[1] + b[1]) / 2), (a[0] + 0.5, (a[1] + b[1]) / 2))
    return (((a[0] + b[0]) / 2, a[1] - 0.5), ((a[0] + b[0]) / 2, a[1] + 0.5))


def get_side_ortho(side: Side, down_factor: int, side_factor: int = 0) -> Side:
    same_side = 0 if side[0][0] == side[1][0] else 1

    ans = [[0., 0.], [0., 0.]]
    ans[0][1 - same_side] = side[down_factor][1 - same_side]
    ans[1][1 - same_side] = side[down_factor][1 - same_side]
    ans[0][same_side] = side[0][same_side] - 1 + side_factor
    ans[1][same_side] = side[0][same_side] + side_factor

    return ((ans[0][0], ans[0][1]), (ans[1][0], ans[1][1]))


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
            sides = set()
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
                        sides.add(get_neighbor_side(elem, neigh))
                    else:
                        sides.remove(get_neighbor_side(elem, neigh))

                for neigh in neighbors_of(elem):
                    q.append(neigh)

            perimeter = 0

            visited_sides = set()
            for side in sides:
                if side in visited_sides:
                    continue
                visited_sides.add(side)
                perimeter += 1

                same_side = 0 if side[0][0] == side[1][0] else 1
                up_side = side
                down_side = side

                while get_side_ortho(up_side, 0, 0) not in sides and get_side_ortho(up_side, 0, 1) not in sides:
                    up_side_l = [list(p) for p in up_side]
                    up_side_l[0][1 - same_side] -= 1
                    up_side_l[1][1 - same_side] -= 1

                    up_side = ((up_side_l[0][0], up_side_l[0][1]),
                               (up_side_l[1][0], up_side_l[1][1]))
                    visited_sides.add(up_side)

                while get_side_ortho(down_side, 1, 0) not in sides and get_side_ortho(down_side, 1, 1) not in sides:
                    down_side_l = [list(p) for p in down_side]
                    down_side_l[0][1 - same_side] += 1
                    down_side_l[1][1 - same_side] += 1

                    down_side = (
                        (down_side_l[0][0], down_side_l[0][1]), (down_side_l[1][0], down_side_l[1][1]))
                    visited_sides.add(down_side)

            ans += area * perimeter

    print(ans)
