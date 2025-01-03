#!/usr/bin/env python3

# NOTE: Takes about 11 seconds

from itertools import product
from sys import stdin


def mul_by(rhs: int) -> int:
    ans = 10
    while ans <= rhs:
        ans *= 10
    return ans


if __name__ == "__main__":
    text = stdin.read().splitlines()

    data = []
    for line in text:
        fields = line.split(": ")
        data.append((int(fields[0]), [int(num)
                    for num in fields[1].split(" ")]))

    ans = 0
    for term, nums in data:
        for ops in product("+*|", repeat=(len(nums) - 1)):
            det = nums[0]
            for i in range(len(ops)):
                if ops[i] == "+":
                    det += nums[i + 1]
                elif ops[i] == "|":
                    det = det * mul_by(nums[i + 1]) + nums[i + 1]
                else:
                    det *= nums[i + 1]
            if det == term:
                ans += term
                break

    print(ans)
