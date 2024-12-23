#!/usr/bin/env python3

from sys import stdin

PRUNE = 16777216


def next_step(num: int) -> int:
    num = (num ^ (num * 64)) % PRUNE
    num = (num ^ (num // 32)) % PRUNE
    num = (num ^ (num * 2048)) % PRUNE
    return num


if __name__ == "__main__":
    nums = [int(num) for num in stdin.read().splitlines()]

    ans = 0
    for num in nums:
        for _ in range(2000):
            num = next_step(num)
        ans += num

    print(ans)
