#!/usr/bin/env python3

from sys import stdin

if __name__ == "__main__":
    text = stdin.read().splitlines()

    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_delta = 0

    ans = -1
    for i in range(len(text)):
        for j in range(len(text[0])):
            if text[i][j] == "^":
                start = (i, j)
                break

    def get_next_pos():
        return (start[0] + deltas[current_delta][0], start[1] + deltas[current_delta][1])

    poses = {start}
    while ans < 0:
        while True:
            next_pos = get_next_pos()
            if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= len(text) or next_pos[1] >= len(text[0]):
                ans = len(poses)
                break
            if text[next_pos[0]][next_pos[1]] != "#":
                break
            current_delta = (current_delta + 1) % 4
        poses.add(next_pos)
        start = next_pos

    print(ans)
