#!/usr/bin/env python3

# NOTE: Takes about 8 seconds

from sys import stdin
from typing import Optional

if __name__ == "__main__":
    text = stdin.read().splitlines()

    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    ans = 0
    for i in range(len(text)):
        for j in range(len(text[0])):
            if text[i][j] == "^":
                start = (i, j)
                break

    def get_poses(start: tuple[int, int], obstacle: Optional[tuple[int, int]] = None) -> tuple[set[tuple[int, int]], bool]:
        curr_point = start
        current_delta = 0

        def get_next_pos():
            return (curr_point[0] + deltas[current_delta][0], curr_point[1] + deltas[current_delta][1])

        poses = set()
        while True:
            while True:
                next_pos = get_next_pos()
                if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= len(text) or next_pos[1] >= len(text[0]):
                    return (poses if obstacle is None else set(), False)
                if text[next_pos[0]][next_pos[1]] != "#" and next_pos != obstacle:
                    break
                current_delta = (current_delta + 1) % 4

            if obstacle is None:
                poses.add(next_pos)
            else:
                if (next_pos, current_delta) in poses:
                    return set(), True
                poses.add((next_pos, current_delta))

            curr_point = next_pos

    poses, _ = get_poses(start)
    for pos in poses:
        if get_poses(start, pos)[1]:
            ans += 1
    print(ans)
