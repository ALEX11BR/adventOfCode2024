#!/usr/bin/env python3

import heapq
from sys import stdin
from typing import Generator


def subtract_points(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
    return (p1[0] - p2[0], p1[1] - p2[1])


def directions() -> Generator[tuple[int, int], None, None]:
    for k in range(4):
        new_point = [0, 0]
        new_point[k // 2] = (-1) ** (k % 2)
        yield (new_point[0], new_point[1])


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
        dist: dict[tuple[tuple[int, int], tuple[int, int]], int] = {}
        logs: dict[tuple[tuple[int, int], tuple[int, int]],
                   set[tuple[int, int]]] = {}
        q: list[tuple[int, tuple[int, int],
                      tuple[int, int], set[tuple[int, int]]]] = []
        heapq.heappush(q, (0, point, (0, 1), set()))

        while q:
            dist_to, elem, direction, log = heapq.heappop(q)
            if (elem, direction) in dist:
                if dist_to == dist[elem, direction]:
                    logs[elem, direction] |= log
                continue
            dist[elem, direction] = dist_to
            logs[elem, direction] = log | {elem}

            for neigh in neighbors_of(elem):
                if subtract_points(elem, neigh) == direction:
                    continue
                if subtract_points(neigh, elem) == direction:
                    heapq.heappush(
                        q, (dist_to + 1, neigh, direction, logs[elem, direction]))
                else:
                    heapq.heappush(
                        q, (dist_to + 1001, neigh, subtract_points(neigh, elem), logs[elem, direction]))

        end = (1, len(text[0]) - 2)
        to_consider = logs[end, (-1, 0)]
        if dist[end, (0, 1)] < dist[end, (-1, 0)]:
            to_consider = logs[end, (0, 1)]
        elif dist[end, (0, 1)] == dist[end, (-1, 0)]:
            to_consider |= logs[end, (0, 1)]

        """
        for i in range(len(text)):
            for j in range(len(text[0])):
                if (i, j) in to_consider:
                    print("O", end="")
                else:
                    print(text[i][j], end="")
            print()
        """

        return len(to_consider)

    ans = dijkstra((len(text) - 2, 1))

    print(ans)
