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


def box_of(pos: tuple[int, int], elem: str) -> tuple[tuple[int, int], tuple[int, int]]:
    if elem == "[":
        return pos, (pos[0], pos[1] + 1)
    else:
        return (pos[0], pos[1] - 1), pos


if __name__ == "__main__":
    world = []
    actions = ""

    in_world = True

    for line in stdin:
        line = line.strip()

        if not line:
            in_world = False
        elif in_world:
            world.append(list(line.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")))
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

        new_start = move_point(start, direction)
        can_move = True
        if world[new_start[0]][new_start[1]] in "[]":
            boxes_to_move = {box_of(new_start, world[new_start[0]][new_start[1]])}
            new_boxes = set(boxes_to_move)

            while new_boxes and can_move:
                new_new_boxes = set()
                for box in new_boxes:
                    for point in box:
                        new_point = move_point(point, direction)
                        if world[new_point[0]][new_point[1]] == "#":
                            can_move = False
                        if world[new_point[0]][new_point[1]] not in "[]":
                            continue

                        new_box = box_of(new_point, world[new_point[0]][new_point[1]])
                        if new_box not in boxes_to_move:
                            boxes_to_move.add(new_box)
                            new_new_boxes.add(new_box)
                new_boxes = new_new_boxes

            if can_move:
                for box in boxes_to_move:
                    for i, j in box:
                        world[i][j] = "."
                for box in boxes_to_move:
                    i1, j1 = move_point(box[0], direction)
                    i2, j2 = move_point(box[1], direction)

                    world[i1][j1] = "["
                    world[i2][j2] = "]"
        else:
            can_move = world[new_start[0]][new_start[1]] != "#"

        if can_move:
            world[start[0]][start[1]] = "."
            world[new_start[0]][new_start[1]] = "@"
            start = new_start

    for i in range(len(world)):
        for j in range(len(world[0])):
            if world[i][j] == "[":
                ans += 100 * i + j

    print(ans)
