#!/usr/bin/env python3

from sys import stdin

if __name__ == "__main__":
    text = stdin.read().splitlines()

    fields = [line.split() for line in text]
    nums = [[int(field[i]) for i in range(2)] for field in fields]

    nums0 = sorted([num[0] for num in nums])
    nums1 = sorted([num[1] for num in nums])

    ans = sum([abs(nums0[i] - nums1[i]) for i in range(len(nums0))])

    print(ans)
