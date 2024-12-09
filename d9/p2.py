#!/usr/bin/env python3

# NOTE: takes about 3 seconds (using CPython)


def sum_range(start: int, end: int) -> int:
    return int(end * (end + 1) / 2 - start * (start - 1) / 2)


if __name__ == "__main__":
    text = [int(c) for c in input()]

    ans = 0

    free_spaces = []
    positions = []
    position = 0
    for i in range(len(text)):
        positions.append(position)
        if i % 2 == 1:
            free_spaces.append([position, text[i]])
        position += text[i]

    for i in range(len(text) - 1, -1, -2):
        done = False
        for j in range(len(free_spaces)):
            if free_spaces[j][0] > positions[i]:
                break
            if free_spaces[j][1] >= text[i]:
                ans += (i // 2) * \
                    sum_range(free_spaces[j][0],
                              free_spaces[j][0] + text[i] - 1)
                free_spaces[j][0] += text[i]
                free_spaces[j][1] -= text[i]
                done = True
                break
        if not done:
            ans += (i // 2) * \
                sum_range(positions[i], positions[i] + text[i] - 1)

    print(ans)
