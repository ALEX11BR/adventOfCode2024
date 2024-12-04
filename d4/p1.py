#!/usr/bin/env python3

from sys import stdin

if __name__ == "__main__":
    text = stdin.read().splitlines()

    ans = 0
    lo = ["XMAS", "SAMX"]

    for i in range(len(text)):
        for j in range(len(text[0]) - 3):
            if text[i][j:j+4] in lo:
                ans += 1
    for i in range(len(text) - 3):
        for j in range(len(text[0])):
            if "".join([text[k][j] for k in range(i, i+4)]) in lo:
                ans += 1
    for i in range(len(text) - 3):
        for j in range(len(text[0]) - 3):
            if "".join([text[i + k][j + k] for k in range(4)]) in lo:
                ans += 1
            if "".join([text[i + 3 - k][j + k] for k in range(4)]) in lo:
                ans += 1

    print(ans)
