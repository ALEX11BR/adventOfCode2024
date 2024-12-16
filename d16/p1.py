#!/usr/bin/env python3

import heapq
from sys import stdin
from typing import Generator


def subtract_points(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
    return (p1[0] - p2[0], p1[1] - p2[1])


if __name__ == "__main__":
    text = stdin.read().splitlines()

    def neighbors_of(point: tuple[int, int]) -> Generator[tuple[int, int], None, None]:
        for k in range(4):
            new_point = list(point)
            new_point[k // 2] += (-1) ** (k % 2)
            if text[new_point[0]][new_point[1]] == "#":
                continue
            yield (new_point[0], new_point[1])

    def dijkstra(point: tuple[int, int]) -> int:
        dist = {}
        q: list[tuple[int, tuple[int, int], tuple[int, int]]] = []
        heapq.heappush(q, (0, point, (0, 1)))

        while q:
            dist_to, elem, direction = heapq.heappop(q)
            if (elem, direction) in dist:
                continue
            dist[elem, direction] = dist_to
            if text[elem[0]][elem[1]] == "E":
                return dist_to

            for neigh in neighbors_of(elem):
                if subtract_points(elem, neigh) == direction:
                    continue
                if subtract_points(neigh, elem) == direction:
                    heapq.heappush(q, (dist_to + 1, neigh, direction))
                else:
                    heapq.heappush(q, (dist_to + 1001, neigh,
                                   subtract_points(neigh, elem)))
        return -1

    ans = dijkstra((len(text) - 2, 1))

    print(ans)
