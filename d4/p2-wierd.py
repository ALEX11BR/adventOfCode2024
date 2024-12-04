#!/usr/bin/env python3

from sys import stdin

if __name__ == "__main__":
    text = stdin.read().splitlines()

    ans = 0

    for i in range(1, len(text) - 1):
        for j in range(1, len(text[0]) - 1):
            if text[i][j] != "A":
                continue
            if f"{text[i - 1][j - 1]}{text[i + 1][j + 1]}" not in ["MS, SM"]:
                continue
            if f"{text[i + 1][j - 1]}{text[i - 1][j + 1]}" not in ["MS, SM"]:
                continue
            ans += 1

    print(ans)
