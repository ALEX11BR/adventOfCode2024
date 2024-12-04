#!/usr/bin/env python3

from sys import stdin

if __name__ == "__main__":
    text = stdin.read().splitlines()

    ans = 0
    lo = ["SM", "MS"]

    for i in range(1, len(text) - 1):
        for j in range(1, len(text[0]) - 1):
            if text[i][j] != "A":
                continue
            diag1 = f"{text[i - 1][j - 1]}{text[i + 1][j + 1]}"
            diag2 = f"{text[i + 1][j - 1]}{text[i - 1][j + 1]}"
            if diag1 in lo and diag2 in lo:
                ans += 1

    print(ans)
