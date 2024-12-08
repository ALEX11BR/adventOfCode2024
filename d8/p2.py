#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin


def get_far_point(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
    delta = (p2[0] - p1[0], p2[1] - p1[1])
    return (p2[0] + delta[0], p2[1] + delta[1])


if __name__ == "__main__":
    text = stdin.read().splitlines()

    points = set()

    def maybe_add(point: tuple[int, int]):
        if point[0] < 0 or point[1] < 0 or point[0] >= len(text) or point[1] >= len(text[0]):
            return False
        points.add(point)
        return True

    freqs = defaultdict(list)
    for i in range(len(text)):
        for j in range(len(text[0])):
            if text[i][j] != ".":
                points.add((i, j))
                for other in freqs[text[i][j]]:
                    point_a = other
                    point_b = (i, j)
                    far = get_far_point(point_a, point_b)
                    while maybe_add(far):
                        point_a = point_b
                        point_b = far
                        far = get_far_point(point_a, point_b)

                    point_b = other
                    point_a = (i, j)
                    far = get_far_point(point_a, point_b)
                    while maybe_add(far):
                        point_a = point_b
                        point_b = far
                        far = get_far_point(point_a, point_b)
                freqs[text[i][j]].append((i, j))

    ans = len(points)

    print(ans)
