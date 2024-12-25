#!/usr/bin/env python3

from collections import defaultdict


def simulate_rock(rock: str) -> list[str]:
    if rock == "0":
        return ["1"]
    elif len(rock) % 2 == 0:
        h1 = rock[:(len(rock) // 2)]

        h2 = rock[(len(rock) // 2):]
        while len(h2) > 1 and h2[0] == "0":
            h2 = h2[1:]

        return [h1, h2]
    else:
        return [str(int(rock) * 2024)]


if __name__ == "__main__":
    nums = input().strip().split(" ")

    stones: defaultdict[str, int] = defaultdict(int)
    for num in nums:
        stones[num] += 1

    for _ in range(75):
        new_stones: defaultdict[str, int] = defaultdict(int)
        for stone in stones:
            for new_stone in simulate_rock(stone):
                new_stones[new_stone] += stones[stone]
        stones = new_stones

    ans = sum(stones.values())
    print(ans)
