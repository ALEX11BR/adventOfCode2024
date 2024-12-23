#!/usr/bin/env python3

# NOTE: takes about 14 seconds

from sys import stdin

PRUNE = 16777216


def next_step(num: int) -> int:
    num = (num ^ (num * 64)) % PRUNE
    num = (num ^ (num // 32)) % PRUNE
    num = (num ^ (num * 2048)) % PRUNE
    return num


if __name__ == "__main__":
    nums = [int(num) for num in stdin.read().splitlines()]
    yields = []
    combs: set[tuple[int, ...]] = set()

    ans = 0
    for num in nums:
        prices_num = [num % 10]
        yields_num = {}
        for _ in range(2000):
            num = next_step(num)
            prices_num.append(num % 10)

            if len(prices_num) >= 5:
                trigger = tuple([prices_num[x] - prices_num[x - 1]
                                for x in range(-4, 0)])
                if trigger not in yields_num:
                    yields_num[trigger] = num % 10

        yields.append(yields_num)
        combs.update(yields_num)

    for comb in combs:
        ans = max(ans, sum([yields_num.get(comb, 0) for yields_num in yields]))

    print(ans)
