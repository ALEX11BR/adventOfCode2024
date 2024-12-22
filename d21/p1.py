#!/usr/bin/env python3

from sys import stdin
from typing import Callable


def get_moves(pos1: tuple[int, int], pos2: tuple[int, int], symbol_world: bool) -> str:
    """
    # Buggy implementation that works for part 1
    ans = ""
    p1 = list(pos1)
    p2 = list(pos2)

    compo1 = ""
    compo2 = ""
    while p1[1] != p2[1]:
        compo1 += ">" if p1[1] < p2[1] else "<"
        p1[1] += 1 if p1[1] < p2[1] else -1
    while p1[0] != p2[0]:
        compo2 += "v" if p1[0] < p2[0] else "^"
        p1[0] += 1 if p1[0] < p2[0] else -1

    if symbol_world:
        if pos1[0] == 0 and pos2[1] == 0:
            ans = compo2 + compo1
        else:
            ans = compo1 + compo2
    else:
        line_first = True

        if pos1[0] == 3 and pos2[1] == 0:
            line_first = False

        line_act = ">" if pos1[1] < pos2[1] else "<"
        if line_act != "<":
            line_first = False

        if pos1[1] == 0 and pos2[0] == 3:
            line_first = True

        if line_first:
            ans = compo1 + compo2
        else:
            ans = compo2 + compo1

    return ans
    """
    ans = ""
    p1 = list(pos1)
    p2 = list(pos2)

    compo1 = ""
    compo2 = ""
    while p1[1] != p2[1]:
        compo1 += ">" if p1[1] < p2[1] else "<"
        p1[1] += 1 if p1[1] < p2[1] else -1
    while p1[0] != p2[0]:
        compo2 += "v" if p1[0] < p2[0] else "^"
        p1[0] += 1 if p1[0] < p2[0] else -1

    line_first = True

    if not symbol_world and pos1[0] == 3 and pos2[1] == 0:
        line_first = False
    if symbol_world and pos2[1] == 0 and pos1[0] == 0:
        line_first = False

    line_act = ">" if pos1[1] < pos2[1] else "<"
    if line_act != "<":
        line_first = False

    if not symbol_world and pos1[1] == 0 and pos2[0] == 3:
        line_first = True
    if symbol_world and pos2[0] == 0 and pos1[1] == 0:
        line_first = True

    if line_first:
        ans = compo1 + compo2
    else:
        ans = compo2 + compo1

    return ans


def digit_position(digit: str) -> tuple[int, int]:
    match digit:
        case "A":
            return 3, 2
        case "0":
            return 3, 1
        case _:
            val = int(digit) - 1
            return 2 - val // 3, val % 3


def arrow_position(elem: str) -> tuple[int, int]:
    match elem:
        case "<":
            return 1, 0
        case ">":
            return 1, 2
        case "^":
            return 0, 1
        case "v":
            return 1, 1
        case _:
            return 0, 2


def indirect_arrows(arrows: str, position: Callable[[str], tuple[int, int]] = arrow_position) -> str:
    ans = ""
    last = "A"

    for char in arrows:
        pos1 = position(last)
        pos2 = position(char)

        new_moves = get_moves(pos1, pos2, position is arrow_position)
        ans += new_moves + "A"

        last = char

    return ans


if __name__ == "__main__":
    text = stdin.read().splitlines()

    ans = 0

    for code in text:
        moves = indirect_arrows(indirect_arrows(
            indirect_arrows(code, digit_position)))
        ans += int(code[:-1]) * len(moves)

    print(ans)
