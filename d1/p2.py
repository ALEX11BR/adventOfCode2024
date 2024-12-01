#!/usr/bin/env python3

from sys import stdin

if __name__ == "__main__":
    text = stdin.read().splitlines()

    fields = [line.split() for line in text]
    nums = [[int(field[i]) for i in range(2)] for field in fields]

    nums0 = sorted([num[0] for num in nums])
    nums1 = sorted([num[1] for num in nums])

    ans = 0
    for num in nums0:
        occ = 0
        for other in nums1:
            if other == num:
                occ += 1
        ans += occ * num

    print(ans)
