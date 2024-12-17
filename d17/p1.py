#!/usr/bin/env python3

import re

if __name__ == "__main__":
    a_match = re.search("[0-9]+", input())
    b_match = re.search("[0-9]+", input())
    c_match = re.search("[0-9]+", input())

    assert (a_match is not None and b_match is not None and c_match is not None)

    a = int(a_match[0])
    b = int(b_match[0])
    c = int(c_match[0])

    input()
    ops = [int(op[0]) for op in re.finditer("[0-9]+", input())]

    def get_combo(combo: int) -> int:
        if combo < 4:
            return combo
        if combo == 4:
            return a
        if combo == 5:
            return b
        return c

    ans = []

    i = 0
    while i < len(ops):
        new_i = i + 2
        match ops[i]:
            case 0:
                a = a // (1 << get_combo(ops[i + 1]))
            case 1:
                b = b ^ ops[i + 1]
            case 2:
                b = get_combo(ops[i + 1]) & 7
            case 3:
                if a != 0:
                    new_i = ops[i + 1]
            case 4:
                b = b ^ c
            case 5:
                ans.append(str(get_combo(ops[i + 1]) & 7))
            case 6:
                b = a // (1 << get_combo(ops[i + 1]))
            case 7:
                c = a // (1 << get_combo(ops[i + 1]))
        i = new_i

    print(",".join(ans))
