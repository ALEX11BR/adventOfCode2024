#!/usr/bin/env python3

from sys import stdin


def action_dir(action: str) -> tuple[int, int]:
    match action:
        case "^":
            return -1, 0
        case "v":
            return 1, 0
        case ">":
            return 0, 1
        case _:
            return 0, -1


def move_point(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
    return p1[0] + p2[0], p1[1] + p2[1]


if __name__ == "__main__":
    world = []
    actions = ""

    in_world = True

    for line in stdin:
        line = line.strip()

        if not line:
            in_world = False
        elif in_world:
            world.append(list(line))
        else:
            actions += line

    ans = 0
    for i in range(len(world)):
        for j in range(len(world[0])):
            if world[i][j] == "@":
                start = i, j
                break

    for action in actions:
        direction = action_dir(action)

        test_point = move_point(start, direction)
        while world[test_point[0]][test_point[1]] == "O":
            test_point = move_point(test_point, direction)

        if world[test_point[0]][test_point[1]] != "#":
            new_start = move_point(start, direction)

            if world[new_start[0]][new_start[1]] == "O":
                world[test_point[0]][test_point[1]] = "O"
            world[start[0]][start[1]] = "."
            world[new_start[0]][new_start[1]] = "@"

            start = new_start

    for i in range(len(world)):
        for j in range(len(world[0])):
            if world[i][j] == "O":
                ans += 100 * i + j

    print(ans)
